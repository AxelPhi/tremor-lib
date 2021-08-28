from pytest import fail

from tremor.eventbus import EventBus
from tremor.eventbus.events import BaseEvent

listener_count = 0


def test_simple_filter_apply():
    eventbus = EventBus()

    filter_match = {"source": "chat"}

    def listen_match(event: BaseEvent):
        global listener_count
        listener_count += 1
        assert event.source == "chat"

    eventbus.listen(listen_match, filter_match)

    filter_non_match = {"source": "not_chat"}

    def listen_non_match(event: BaseEvent):
        fail("The non-matching listener should not be called")

    eventbus.listen(listen_non_match, filter_non_match)

    test_event = BaseEvent(id=0, source="chat")
    eventbus.publish(test_event)
    global listener_count
    assert listener_count == 1
