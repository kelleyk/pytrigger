from __future__ import division, absolute_import, unicode_literals, print_function

import logging

from .evented import EventedMixin

log = logging.getLogger(__name__)

class EventedWrapper(EventedMixin):
    def __init__(self, obj):
        self.obj = obj

    def __get__(self):
        self._trigger('get')
        return self.obj

    def __set__(self, obj):
        self._trigger('set')
        self.obj = obj

    def __delete__(self):
        self._trigger('delete')
        del self.obj
        self.obj = None

def evented(obj):
    return EventedWrapper(obj)
