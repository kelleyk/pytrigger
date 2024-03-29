from __future__ import division, absolute_import, unicode_literals, print_function

import logging

log = logging.getLogger(__name__)

class HookedList(list):

    def on_add(self, idx, value):
        pass

    def on_remove(self, idx, value):
        pass

    def on_change(self, idx, value, old_value):
        pass

    def on_set(self):
        pass
   
# __set__

# ['__add__',
#  '__class__',
#  '__contains__',
#  '__delattr__',
#  '__delitem__',
#  '__delslice__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getitem__',
#  '__getslice__',
#  '__gt__',
#  '__hash__',
#  '__iadd__',
#  '__imul__',
#  '__init__',
#  '__iter__',
#  '__le__',
#  '__len__',
#  '__lt__',
#  '__mul__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__reversed__',
#  '__rmul__',
#  '__setattr__',
#  '__setitem__',
#  '__setslice__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'append',
#  'count',
#  'extend',
#  'index',
#  'insert',
#  'pop',
#  'remove',
#  'reverse',
#  'sort']
