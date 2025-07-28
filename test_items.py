from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    try:
        add_to_basket_button = browser.find_element(By.XPATH, '//button[contains(@class,"btn-add-to-basket")]')
        assert add_to_basket_button is not None, "Add to basket button is not shown on the page"
    except NoSuchElementException:
        assert False, "No Add to basket button found"
