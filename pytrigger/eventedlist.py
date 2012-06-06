from __future__ import division, absolute_import, unicode_literals, print_function

import logging

log = logging.getLogger(__name__)

class EventedList(EventedMixin):
    def __init__(self, seq=None):
        self.contents = list(seq)

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, key):
        return self.contents[key]

    def __iter__(self):
        return self.contents.iterkeys()

    def iterkeys(self):
        return self.contents.iterkeys()

    def __contains__(self, item):
        return item in self.contents

    def __set__(self, instance, value):
        self.contents = value

    
