from __future__ import division, absolute_import, unicode_literals, print_function

import logging

log = logging.getLogger(__name__)

__all__ = ('DelayedEventMixin,')

class DelayedEventMixin(object):
    """Adds event buffering abilities to a class."""

    def __init__(self, *args, **kwargs):
        super(DelayedEventMixin, self).__init__(*args, **kwargs)
        self._pending_events = []

    def _delay(self, event, *args, **kwargs):
        """Buffers an event, which will be triggered when _flush() is
        called.  The event will be received by the handlers who are
        registered when _flush() is called, not those who are
        registered when _delay() is called."""
        self._pending_events.append((event, args, kwargs))

    def _clear_pending(self):
        """Removes all delayed events without triggering them."""
        self._pending_events = []

    def _trigger_pending(self):
        """Triggers all delayed events."""

        log.debug('Triggering {0} pending event(s).'\
                      .format(len(self._pending_events)))
        for event, args, kwargs in self._pending_events:
            self._trigger(event, *args, **kwargs)
        self._pending_events = []
