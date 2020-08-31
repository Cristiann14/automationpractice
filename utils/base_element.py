from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locator import Locator
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        #self.by = by
        self.web_element = None
        self.find()


#   visibility_of_element_located
    def find(self):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator=self.locator))
        #element = self.driver.find_element(by=self.by, value=self.locator)
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    @property
    def text(self):
        text_to_get = self.web_element.text
        return text_to_get

    def option(self, option):

        element = Select(self.web_element)
        element.select_by_visible_text(option)
        return None
