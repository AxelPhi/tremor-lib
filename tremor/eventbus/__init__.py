from typing import Callable

from tremor.eventbus.events import BaseEvent


class EventBus:
    def __init__(self):
        self.listeners = []

    def publish(self, event: BaseEvent):
        for listener in self._determine_listeners(event):
            listener(event)

    def listen(
        self, listener: Callable[[BaseEvent], None], event_filter: dict = None
    ):
        self.listeners.append((event_filter, listener))
        pass

    def _determine_listeners(self, event: BaseEvent):
        # Simple serial filter test.
        # Ok for now. Might be too slow for complexer scenarios
        for filter_definition, listener in self.listeners:
            if filter_definition is None:
                yield listener
            if self._filter_matches(filter_definition, event):
                yield listener

    @staticmethod
    def _filter_matches(filter_definition: dict, event: BaseEvent):
        try:
            if event.source == filter_definition.get("source"):
                return True
        except Exception:
            return False
