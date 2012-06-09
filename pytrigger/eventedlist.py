from __future__ import division, absolute_import, unicode_literals, print_function

import logging

log = logging.getLogger(__name__)

from .evented import EventedMixin
from .hookedlist import HookedList

    # TODO: evented list should provide item's index with events
class EventedList(EventedMixin, HookedList):
    def on_add(self, idx, value):
        pass

    def on_remove(self, idx, value):
        pass

    def on_change(self, idx, value, old_value):
        pass

    def on_set(self):
        pass
