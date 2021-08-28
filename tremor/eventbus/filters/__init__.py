from tremor.eventbus import BaseEvent


class PassThroughFilter:
    def filter(self, event: BaseEvent):
        return True


class SourceFilter:
    def __init__(self, source: str):
        self.source = source

    def filter(self, event: BaseEvent):
        return event.source == self.source
