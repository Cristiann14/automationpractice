from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.locator import Locator
from utils.base_element import BaseElement

from utils.base_page import BasePage


class ShippingPage(BasePage):

    @property
    def checkbox_terms(self):
        locator = Locator(By.ID, value='uniform-cgv')
        return BaseElement(self.driver, locator=locator)

    @property
    def btn_submit(self):
        locator = Locator(By.CLASS_NAME, value='button btn btn-default')
        return BaseElement(self.driver, locator=locator)

    @property
    def btn_continue_shopping(self):
        locator = Locator(By.CLASS_NAME, value='button-exclusive btn btn-default')
        return BaseElement(self.driver, locator=locator)

    @property
    def page_heading(self):
        locator = Locator(By.XPATH, value='//*[@id="carrier_area"]/h1')
        return BaseElement(self.driver, locator=locator)

    # ERRORS
    @property
    def uncheked_terms(self):
        locator = Locator(By.CLASS_NAME, value='fancybox-error')
        return BaseElement(self.driver, locator=locator)
