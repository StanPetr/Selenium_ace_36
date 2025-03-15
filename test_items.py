from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
import time


def test_page_has_add_to_basket_button(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    browser.get(link)
    time.sleep(10)
    
    add_button = browser.find_element(By.CLASS_NAME, "btn.btn-add-to-basket")
    
    assert add_button, 'Button Add to basket not found'