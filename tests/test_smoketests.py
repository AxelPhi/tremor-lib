import asyncio

import pytest

from tremor import main_routine
from tremor.eventbus import EventBus
from tremor.events import BaseEvent


@pytest.mark.asyncio
async def test_connector_discovery_is_mocked(connector_discover_mock):
    await main_routine()
    connector_discover_mock.assert_called_once()


@pytest.mark.asyncio
async def test_basic_eventhandling_works(connector_discover_mock):
    test_bus = EventBus()
    test_event = BaseEvent(source="test")
    await test_bus.publish(test_event)
    result = await test_bus.listen()
    assert result == test_event


@pytest.mark.asyncio
async def test_basic_eventtimeout_works(connector_discover_mock):
    test_bus = EventBus()
    try:
        _ = await test_bus.listen(timeout=0.5)
    except asyncio.TimeoutError:
        pass
    else:
        pytest.fail("Should have caused a TimeoutError")
