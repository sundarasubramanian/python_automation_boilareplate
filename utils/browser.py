from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def create_driver(browser='chrome', headless=True):
    if browser.lower() == 'chrome':
        opts = ChromeOptions()
        if headless:
            opts.add_argument('--headless=new')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=opts)
    elif browser.lower() == 'firefox':
        opts = FirefoxOptions()
        if headless:
            opts.add_argument('-headless')
        driver = webdriver.Firefox(options=opts)
    else:
        raise ValueError('Unsupported browser: ' + browser)

    driver.maximize_window()
    return driver
