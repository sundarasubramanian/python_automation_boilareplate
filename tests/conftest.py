import os
import pytest
from utils.browser import create_driver
from utils.config_reader import read_config
from utils.screenshot import save_screenshot


@pytest.fixture(scope='session')
def config():
    cfg = read_config()
    return cfg


@pytest.fixture()
def driver(request, config):
    # Allow environment variables to override config.ini for CI or local runs
    browser = os.environ.get('BROWSER') or config.get('browser', 'chrome')
    headless_env = os.environ.get('HEADLESS')
    if headless_env is None:
        headless = config.getboolean('headless', True)
    else:
        headless = str(headless_env).lower() in ('1', 'true', 'yes')

    drv = create_driver(browser=browser, headless=headless)

    yield drv

    # Teardown: capture screenshot on failure
    # pytest_runtest_makereport sets rep_call on the item
    rep = getattr(request.node, 'rep_call', None)
    if rep and rep.failed:
        try:
            save_screenshot(drv, name_prefix='failure')
        except Exception:
            pass
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
