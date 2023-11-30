from selenium.webdriver.common.by import By
link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_languages(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    print(button.get_attribute("value"))
    assert button.is_displayed()

