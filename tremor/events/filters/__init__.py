import abc
from abc import ABC

from tremor.eventbus import BaseEvent


class BaseFilter(ABC):
    @abc.abstractmethod
    def filter(self, event: BaseEvent):
        pass


class PassThroughFilter(BaseFilter):
    def filter(self, event: BaseEvent):
        return True


class SourceFilter(BaseFilter):
    def __init__(self, source: str):
        self.source = source

    def filter(self, event: BaseEvent):
        return event.source == self.source
