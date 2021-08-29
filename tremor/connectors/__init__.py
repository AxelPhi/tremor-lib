import importlib
import pkgutil

PLUGIN_PREFIX = "tremor_connector"


def collect_internal_connectors() -> dict:
    import tremor.connectors.dummy as tremor_connector_dummy

    return {tremor_connector_dummy.__name__: tremor_connector_dummy}


def discover_external_connectors() -> dict:
    return {
        name: importlib.import_module(name)
        for finder, name, ispkg in pkgutil.iter_modules()
        if name.startswith(PLUGIN_PREFIX)
    }


def get_connectors() -> dict:
    connectors = collect_internal_connectors()
    connectors.update(discover_external_connectors())
    return connectors


__all__ = ["get_connectors"]
