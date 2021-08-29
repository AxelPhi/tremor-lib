from tremor.events import BaseEvent
from tremor.events.filters import (
    CategoryFilter,
    PassThroughFilter,
    SourceFilter,
)


def test_passthrough_filter():
    base_event = BaseEvent(source="test")
    assert PassThroughFilter().filter(base_event)


def test_source_filter():
    base_event = BaseEvent(source="test")

    assert SourceFilter("test").filter(base_event)
    assert not SourceFilter("non_test").filter(base_event)

    assert SourceFilter(["test"]).filter(base_event)
    assert not SourceFilter(["non_test"]).filter(base_event)


def test_category_filter():
    base_event = BaseEvent(source="test")

    assert CategoryFilter("base").filter(base_event)
    assert not CategoryFilter("non_base").filter(base_event)

    assert CategoryFilter(["base"]).filter(base_event)
    assert not CategoryFilter(["non_base"]).filter(base_event)
