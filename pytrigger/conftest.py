from __future__ import division, absolute_import, unicode_literals, print_function

import logging

log = logging.getLogger(__name__)

from . import evented
from . import wrapper

evented.callback_wrapper = evented.unsafe_callback_wrapper

class TestTrace(object):
    def __init__(self):
        self.contents = []

    def callback(self, label):
        def _callback(*args, **kwargs):
            self.contents.append((label, args, kwargs))
        return _callback

    def __eq__(self, other):
        return self.contents == other

    def __ne__(self, other):
        return self.contents != other

    def __repr__(self):
        return repr(self.contents)


def pytest_funcarg__obj(request):
    evented.callback_wrapper = evented.unsafe_callback_wrapper
    return evented.EventedMixin()

def pytest_funcarg__wrapped(request):
    return wrapper.evented('wrapped string')

def pytest_funcarg__tr(request):
    return TestTrace()
