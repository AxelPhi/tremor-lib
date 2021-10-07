import logging

from tremor.eventbus import EventBus

log = logging.getLogger(__name__)


async def init(event_bus: EventBus):
    log.info("Initialized test connector")
