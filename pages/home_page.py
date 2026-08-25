"""Page object for the application's home page."""

from pages.base_page import BasePage

class HomePage(BasePage):
    """Page object for the application's home page."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.url = 'https://example.com'

    def open(self):
        self.visit(self.url)

    def has_example_text(self):
        return 'Example Domain' in self.driver.title
