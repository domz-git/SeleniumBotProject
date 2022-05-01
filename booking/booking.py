from selenium import webdriver
import time
from booking.constants import *

PATH = "C:\SeleniumDrivers\chromedriver.exe"

class Booking():
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
    
    def land_page(self):
        self.driver.get(PAGE_URL)

    def accept_cookies(self):
        accept_button = self.driver.find_element_by_id("onetrust-accept-btn-handler")
        accept_button.click()
        

    def change_currency(self, currency=None):
        currency_element = self.driver.find_element_by_css_selector('button[data-tooltip-text="Choose your currency"]')
        currency_element.click()

        selected_currency = self.driver.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency.click()

    def sleep(self):
        time.sleep(5)
