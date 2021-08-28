from tremor import main_routine


def test_connector_discovery_is_mocked(event_loop, connector_discover_mock):
    event_loop.run_until_complete(main_routine())
    connector_discover_mock.assert_called_once()
