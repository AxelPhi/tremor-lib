import asyncio

from tremor.eventbus import EventBus
from tremor.eventbus.events import ChatEvent


async def sendMsg(eventBus: EventBus):
    for i in range(100):
        eventBus.publish(
            ChatEvent(
                id=0, source="twitch", msg=f"Hello {i}", sender="Twitch Viewer"
            )
        )
        await asyncio.sleep(1)


def init(eventBus: EventBus):
    print("Init Twitch.Tv connector")
    loop = asyncio.get_event_loop()
    loop.create_task(sendMsg(eventBus))
