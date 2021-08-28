import pytest
import testconnector


@pytest.fixture
def connector():
    return testconnector


@pytest.fixture
def connector_discover_mock(mocker, connector):
    return mocker.patch(
        "tremor.get_connectors",
        return_value={"test_connector": connector},
    )
