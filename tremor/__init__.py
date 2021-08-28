import asyncio
import logging

from tremor.connectors import get_connectors

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s"
)

log = logging.getLogger(__name__)


async def main_routine():
    cts = get_connectors()
    if not cts:
        log.warning("No connectors found.")
        return
    log.info("Found connectors...")
    for connector_name, connector in cts.items():
        log.info(f"Found connector: {connector_name} with module {connector}")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_routine())
    #    loop.run_forever()
    loop.close()


if __name__ == "__main__":
    main()
