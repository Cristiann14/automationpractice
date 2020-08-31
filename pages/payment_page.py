from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.locator import Locator
from utils.base_element import BaseElement

from utils.base_page import BasePage


class PaymentPage(BasePage):

    @property
    def pay_by_bank(self):
        locator = Locator(By.CLASS_NAME, value='bankwire')
        return BaseElement(self.driver, locator=locator)

    @property
    def pay_by_check(self):
        locator = Locator(By.CLASS_NAME, value='cheque')
        return BaseElement(self.driver, locator=locator)

    @property
    def page_heading(self):
        locator = Locator(By.XPATH, value='//*[@id="center_column"]/h1')
        return BaseElement(self.driver, locator=locator)

    @property
    def total_price(self):
        locator = Locator(By.ID, value='total_price')
        return BaseElement(self.driver, locator=locator)

    @property
    def total_products(self):
        locator = Locator(By.ID, value='total_product')
        return BaseElement(self.driver, locator=locator)
