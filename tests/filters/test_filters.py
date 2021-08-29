from events import BaseEvent
from events.filters import PassThroughFilter, SourceFilter


def test_passthrough_filter():
    base_event = BaseEvent(source="test")
    assert PassThroughFilter().filter(base_event)


def test_source_filter():
    base_event = BaseEvent(source="test")
    assert SourceFilter("test").filter(base_event)
    assert not SourceFilter("non_test").filter(base_event)
