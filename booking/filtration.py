from selenium import webdriver
import time
from booking.constants import *

class Filtration():

    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
    
    def star_rating(self, stars):
        star_element = self.driver.find_element_by_name(f"class={stars}")

        star_element.click()