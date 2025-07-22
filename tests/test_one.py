from selene import browser, be, have
def test_no_match():
    browser.element('[name="q"]').should(be.visible).type("ыдлвофошывшфоытвофытвшофрывофытовлфтвыь").press_enter()
    (browser.element('[class="gSXOPxXJQAIpv4HDaDFd"]').should
     (have.text('По запросу «adsdasвышгрфыш!№;%га561253!» ничего не найдено.')))