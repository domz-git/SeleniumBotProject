from lib2to3.pgen2 import driver
from selenium.webdriver.remote.webdriver import WebDriver
import time
from booking.constants import *

class Filtration():

    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
    
    def star_rating(self, *stars):
        for star in stars:
            star_element = self.driver.find_element_by_name(f"class={star}")
            star_element.click()
            self.driver.implicitly_wait(15)

    def list_bookings(self):
        bookings = self.driver.find_element_by_id("search_results_table").find_elements_by_css_selector(
            'div[data-testid="property-card"]'
        )
        print(bookings)

    def sleep(self):
        time.sleep(5)