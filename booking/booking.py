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

    def destination(self, destination):
        destination_field = self.driver.find_element_by_id("ss")
        destination_field.clear()
        destination_field.send_keys(destination)
        first_element = self.driver.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_element.click()

    def dates(self, date_check_in, date_check_out):
        date_check_in = self.driver.find_element_by_css_selector(
            f'td[data-date="{date_check_in}"]'
        )
        date_check_in.click()
        date_check_out = self.driver.find_element_by_css_selector(
            f'td[data-date="{date_check_out}"]'
        )
        date_check_out.click()

    def adults(self, count):
        select_adult = self.driver.find_element_by_id("xp__guests__toggle")
        select_adult.click()

        decrease_adults = self.driver.find_elements_by_css_selector



    def sleep(self):
        time.sleep(5)
