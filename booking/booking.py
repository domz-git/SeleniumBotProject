from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from booking.constants import *
from booking.filtration import Filtration

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
        self.driver.implicitly_wait(15)
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

        number_of_adults = self.driver.find_element_by_id("group_adults")
        decrease_adults = self.driver.find_element_by_css_selector(
            'button[aria-label="Decrease number of Adults"]'
        )
        increase_adults = self.driver.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        while(int(number_of_adults.get_attribute('value'))>1):
            decrease_adults.click()
        
        while(int(number_of_adults.get_attribute('value'))<count):
            increase_adults.click()

    def search(self):
        search_button = self.driver.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def filtration(self):
        filtration = Filtration(driver=self.driver)

        filtration.star_rating(2,3)
        filtration.list_bookings()
        filtration.sleep()

    
