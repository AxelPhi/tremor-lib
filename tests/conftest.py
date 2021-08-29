import pytest
import testconnector


@pytest.fixture
def test_connector():
    return testconnector


@pytest.fixture
def connector_discover_mock(mocker, test_connector):
    return mocker.patch(
        "tremor.get_connectors",
        return_value={"test_connector": test_connector},
    )
