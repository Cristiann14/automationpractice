from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.locator import Locator
from utils.base_element import BaseElement

from utils.base_page import BasePage


class AddressPage(BasePage):

#### DELIVERY ADDRESS DROPDOWN SELECTORS ##############
    @property
    def dropdown_delivery_address(self):
        locator = Locator(By.ID, value='id_address_delivery')
        return BaseElement(self.driver, locator=locator)

    @property
    def checkbox_billing_address(self):
        locator = Locator(By.ID, value='addressesAreEquals')
        return BaseElement(self.driver, locator=locator)


    @property
    def btn_delivery_address_update(self):
        locator = Locator(By.CSS_SELECTOR, value='div.row > div:nth-of-type(1)')
        return BaseElement(self.driver, locator=locator)


    @property
    def btn_billing_address_update(self):
        locator = Locator(By.CSS_SELECTOR, value='div.row > div:nth-of-type(2)')
        return BaseElement(self.driver, locator=locator)


    @property
    def btn_add_new_address(self):
        locator = Locator(By.CLASS_NAME, value='address_add submit')
        return BaseElement(self.driver, locator=locator)


    @property
    def input_text_area(self):
        locator = Locator(By.CLASS_NAME, value='form-group')
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
        locator = Locator(By.CSS_SELECTOR, value='#center_column > h1')
        return BaseElement(self.driver, locator=locator)