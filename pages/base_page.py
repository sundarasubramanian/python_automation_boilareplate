from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # type: ignore[reportMissingImports]
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def visit(self, url):
        self.driver.get(url)

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        el = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        el.click()

    def get_text(self, locator):
        el = self.find(locator)
        return el.text

    def title_contains(self, text):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.title_contains(text))
        except TimeoutException:
            return False
