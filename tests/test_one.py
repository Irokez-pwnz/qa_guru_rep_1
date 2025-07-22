import pytest
from selene import browser, be, have


@pytest.fixture(autouse=True)
def browser_size():
 browser.config.window_height = 1366
 browser.config.window_width = 1024
 browser.open('https://duckduckgo.com')
 yield
 browser.quit()


def test_selene_find_text():
 browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
 browser.element('html').should(have.text('Selene'))




def test_selene_impossible_text():
 browser.element('[name="q"]').should(be.blank).type('sadhjlasfhljsdaf').press_enter()
 browser.element('html').should(have.text('По запросу «sadhjlasfhljsdaf» ничего не найдено.'))