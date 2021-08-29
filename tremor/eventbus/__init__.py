import asyncio
from typing import List

from tremor.events import BaseEvent
from tremor.events.filters import BaseFilter


class EventBus:
    def __init__(self):
        self.event_queue = asyncio.Queue()

    async def publish(self, event: BaseEvent):
        await self.event_queue.put(event)

    async def listen(
        self, event_filters: List[BaseFilter] = None, timeout: float = None
    ) -> BaseEvent:
        while True:
            if timeout:
                event = asyncio.wait_for(self.event_queue, timeout)
            else:
                event = await self.event_queue.get()
            for event_filter in event_filters:
                if event_filter.filter(event):
                    return event
