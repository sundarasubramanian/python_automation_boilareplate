import pytest
from utils.browser import create_driver
from utils.config_reader import read_config
from utils.screenshot import save_screenshot

import os

@pytest.fixture(scope='session')
def config():
    cfg = read_config()
    return cfg

@pytest.fixture
def driver(request, config):
    browser = config.get('browser', 'chrome')
    headless = config.getboolean('headless', True)
    drv = create_driver(browser=browser, headless=headless)

    yield drv

    # teardown
    if request.node.rep_call.failed:
        try:
            save_screenshot(drv, name_prefix='failure')
        except Exception:
            pass
    drv.quit()

# hook to set report status on node for teardown
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
