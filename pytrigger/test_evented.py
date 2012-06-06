from __future__ import division, absolute_import, unicode_literals, print_function

class TestsEventedMixin(object):
    def test_event_triggered(self, obj, tr):
        obj.on('bounce', tr.callback('bounce'))
        obj._trigger('bounce')
        assert tr == [('bounce', (), {})]

    def test_event_args(self, obj, tr):
        obj.on('bounce', tr.callback('bounce'))
        obj._trigger('bounce', 42, 'blue')
        assert tr == [('bounce', (42, 'blue'), {})]        

    def test_event_args(self, obj, tr):
        obj.on('bounce', tr.callback('bounce'))
        obj._trigger('bounce', hello='world', answer=42)
        assert tr == [('bounce', (), {'hello': 'world', 'answer': 42})]

    def test_event_args_kwargs(self, obj, tr):
        obj.on('bounce', tr.callback('bounce'))
        obj._trigger('bounce', 'blue', hello='world', answer=42)
        assert tr == [('bounce', ('blue',), {'hello': 'world', 'answer': 42})]

    def test_all_event(self, obj, tr):
        obj.on('all', tr.callback('all'))
        obj._trigger('bounce')
        assert tr == [('all', ('bounce', (), {}), {})]

    def test_data_object_passed(self, obj, tr):
        data = object()
        obj.on('bounce', tr.callback('bounce'), data=data)
        obj._trigger('bounce')
        assert tr == [('bounce', (), {'data': data})]

    def test_off(self, obj, tr):
        callback = tr.callback('bounce')
        obj.on('bounce', callback)
        obj.off('bounce', callback)
        obj._trigger('bounce')
        assert tr == []
