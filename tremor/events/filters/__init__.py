import abc
from abc import ABC
from typing import Iterable, Union

from tremor.eventbus import BaseEvent


class BaseFilter(ABC):
    @abc.abstractmethod
    def filter(self, event: BaseEvent):
        pass


class PassThroughFilter(BaseFilter):
    def filter(self, event: BaseEvent):
        return True


class SourceFilter(BaseFilter):
    def __init__(self, source: Union[str, Iterable[str]]):
        if isinstance(source, str):
            self.source = [source]
        else:
            self.source = source

    def filter(self, event: BaseEvent):
        return event.source in self.source


class CategoryFilter(BaseFilter):
    def __init__(self, category: Union[str, Iterable[str]]):
        if isinstance(category, str):
            self.category = [category]
        else:
            self.category = category

    def filter(self, event: BaseEvent):
        return event.category in self.category
