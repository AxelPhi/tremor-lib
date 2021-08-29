import asyncio
from typing import List, Union

from tremor.events import BaseEvent
from tremor.events.filters import BaseFilter, PassThroughFilter


class EventBus:
    def __init__(self):
        self.event_queue = asyncio.Queue()

    async def publish(self, event: BaseEvent):
        await self.event_queue.put(event)

    async def listen(
        self,
        event_filter: Union[BaseFilter, List[BaseFilter]] = None,
        timeout: float = None,
    ) -> BaseEvent:
        filters = [PassThroughFilter()]
        if event_filter:
            if isinstance(event_filter, BaseFilter):
                filters = [event_filter]
            else:
                filters = event_filter
        while True:
            if timeout:
                event = await asyncio.wait_for(self.event_queue.get(), timeout)
            else:
                event = await self.event_queue.get()
            for event_filter in filters:
                if event_filter.filter(event):
                    return event
