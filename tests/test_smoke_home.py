from pages.home_page import HomePage


def test_home_title(driver):
    home = HomePage(driver)
    home.open()
    assert home.has_example_text(), 'Expected Example Domain in title'
