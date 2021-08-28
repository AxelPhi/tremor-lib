import asyncio

from tremor.connectors import discover_connectors
from tremor.eventbus import EventBus


async def myCoroutine():
    event_bus = EventBus()
    event_bus.listen(lambda x: print(x), None)
    cts = await discover_connectors()
    for connector_name, connector in cts.items():
        print(connector_name)
        try:
            connector.init(event_bus)
        except Exception as exc:
            print(f"Error on init {exc}")


def main():
    global dump_msg
    loop = asyncio.get_event_loop()
    loop.run_until_complete(myCoroutine())
    loop.run_forever()
    loop.close()


if __name__ == "__main__":
    main()
