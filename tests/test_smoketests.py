import pytest

from tremor import main_routine
from tremor.eventbus import EventBus
from tremor.events import BaseEvent
from tremor.events.filters import PassThroughFilter


def test_connector_discovery_is_mocked(event_loop, connector_discover_mock):
    event_loop.run_until_complete(main_routine())
    connector_discover_mock.assert_called_once()


@pytest.mark.asyncio
async def test_basic_eventhandling_works(connector_discover_mock):
    test_bus = EventBus()
    test_event = BaseEvent(source="test")
    test_filter = PassThroughFilter()
    await test_bus.publish(test_event)
    result = await test_bus.listen([test_filter])
    assert result == test_event
