from tremor import main_routine


def test_testconnector(event_loop):
    event_loop.run_until_complete(main_routine())
