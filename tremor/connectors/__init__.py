import importlib
import pkgutil

PLUGIN_PREFIX = "tremor_connector"


async def discover_connectors() -> dict:
    return {
        name: importlib.import_module(name)
        for finder, name, ispkg in pkgutil.iter_modules()
        if name.startswith(PLUGIN_PREFIX)
    }


__all__ = ["discover_connectors"]
