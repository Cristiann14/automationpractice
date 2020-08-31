from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.locator import Locator
from utils.base_element import BaseElement

from utils.base_page import BasePage


class SummaryPage(BasePage):

    #url = 'http://automationpractice.com/index.php?controller=order'

    @property
    def btn_proceed_to_checkout(self):
        locator = Locator(by=By.XPATH, value='//*[@id=\"center_column\"]/p[2]/a[1]/span')
        return BaseElement(self.driver, locator=locator)

    @property
    def input_qty(self):
        locator = Locator(by=By.XPATH, value="//*[@id='product_1_1_0_0']/td[5]/input[2]")
        return BaseElement(self.driver, locator=locator)

    @property
    def btn_add_qty(self):
        locator = Locator(by=By.CLASS_NAME, value='icon-plus')
        return BaseElement(self.driver, locator=locator)


    @property
    def btn_remove_qty(self):
        locator = Locator(by=By.CLASS_NAME, value='icon-minus')
        return BaseElement(self.driver, locator=locator)

    @property
    def btn_trash(self):
        locator = Locator(by=By.CLASS_NAME, value='icon-trash')
        return BaseElement(self.driver, locator=locator)

    @property
    def empty_cart_alert(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#center_column > p')
        return BaseElement(self.driver, locator=locator)

    @property
    def total_price_products(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.price[@id="total_product_price_1_1_0"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def final_price_products(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.price[@id="total_price"]')
        return BaseElement(self.driver, locator=locator)
"""
    @property
    def text_cart_is_empty(self):
        locator = Locator(by=By.CLASS_NAME, value='alert alert-warning')
        return BaseElement(self.driver, locator=locator)
"""
