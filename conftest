import pytest
from selene import browser

@pytest.fixture(scope = 'function' , autouse=True) # Фикстура открытия браузера(1200Х800) и открытие поисковика
def browser_open():
    browser.config.window_width = 1200
    browser.config.window_height = 800
    browser.open('https://duckduckgo.com')
    yield
    browser.quit()