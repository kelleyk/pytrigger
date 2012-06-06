"""Mixin for managing handlers and sending them events."""

from __future__ import division, absolute_import, unicode_literals, print_function

import logging
import collections
import weakref
from functools import partial

from six import text_type, binary_type

log = logging.getLogger(__name__)

__all__ = ('EventedMixin', 'callback_wrapper')

def _to_seq_of_text(x, encoding='ascii'):
    """
    :type x: OneOrSeq[>1](text|binary)
    :rtype: list(text)
    """
    if isinstance(x, (binary_type, text_type)):
        x = (x,)
    return list(map(lambda x: x if isinstance(x, text_type)
                    else x.decode(encoding), x))

def safe_callback_wrapper(handler, *args, **kwargs):
    try:
        handler(*args, **kwargs)    
    except:
        log.error('Callback raised unhandled exception.', exc_info=True)

def unsafe_callback_wrapper(handler, *args, **kwargs):
    handler(*args, **kwargs)    

try:
    import tornado.ioloop
    def ioloop_callback_wrapper(io_loop=None):
        if io_loop is None:
            io_loop = tornado.ioloop.IOLoop.instance()
        def wrapper(handler, *args, **kwargs):
            io_loop.add_callback(lambda: handler(*args, **kwargs))
        return wrapper
except ImportError:
    pass

callback_wrapper = safe_callback_wrapper

class EventedMixin(object):
    """Adds handler management to a class."""

    __invariants__ = (
        ('_handlers', 'dict(text, WeakKeyDictionary)'),
        )

    def __init__(self, *args, **kwargs):
        super(EventedMixin, self).__init__(*args, **kwargs)
        # Maps event name to (handler, data) pairs.
        self._handlers = {}

    def on(self, events, handler, data=None):
        """
        Bind the handler to the event(s) given.  The data object, if
        provided, is passed to each handler as an argument.  A weak
        reference to the handler is kept, but a strong reference to
        the data object is kept.

        :param events: The name of one or more events to listen for.
        :type events: OneOrSeq[>1](text|binary)
        :param handler: The callable that will be invoked when the
            event(s) take place.
        :type handler: callable
        :param data:
        """
        
        events = _to_seq_of_text(events)
        for event in events:
            if event not in self._handlers:
                self._handlers[event] = {}
#                self._handlers[event] = weakref.WeakKeyDictionary()
            self._handlers[event][handler] = data

    def off(self, events, handler):

        events = _to_seq_of_text(events)
        for event in events:
            if event not in self._handlers or handler not in self._handlers[event]:
                log.warning('Handler is not bound to event {}.'.format(event))
                continue
            self._handlers[event].pop(handler)
            if len(self._handlers[event]) == 0:
                del self._handlers[event]

    def _trigger(self, event, *args, **kwargs):
        """Invoke callbacks for handlers who implement callback_name.
        Other arguments are passed on to that function.

        :type event: binary|text
        """

        if isinstance(event, binary_type):
            event = event.decode('ascii')

        if 'data' in kwargs:
            log.warning('Event argument \'data\' will be overwritten.')

        if event in self._handlers:
            for handler, data in self._handlers[event].items():
                if data is None:
                    kwargs.pop('data', None)
                else:
                    kwargs['data'] = data
                callback_wrapper(handler, *args, **kwargs)

        if event != 'all':
            self._trigger('all', event, args, kwargs)
