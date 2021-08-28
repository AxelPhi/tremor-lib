import pytest

from tremor.eventbus import EventBus


@pytest.fixture
def event_bus():
    return EventBus()
