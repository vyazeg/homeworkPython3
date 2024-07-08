from selene import browser, have, be


def test_google():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_no_result():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('asdfafvadvsdfvaasccadsasdc2333fdsfsdf').press_enter()
    browser.element('.card-section').should(have.text('По запросу asdfafvadvsdfvaasccadsasdc2333fdsfsdf ничего не найдено'))
