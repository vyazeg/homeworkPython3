from selene import browser
import pytest


@pytest.fixture(scope="function", autouse=True)
def browser_start():
    browser.open('https://google.com')
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.close()
