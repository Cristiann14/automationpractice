from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.locator import Locator
from utils.base_element import BaseElement

from utils.base_page import BasePage
from pages.summary_page import SummaryPage


class SignPage(BasePage):


    #Create account section
    @property
    def input_email_create(self):
        locator = Locator(by=By.ID, value='email_create')
        return BaseElement(self.driver, locator=locator)

    @property
    def btn_submit_create(self):
        locator = Locator(by=By.ID, value='SubmitCreate')
        return BaseElement(self.driver, locator=locator)

    @property
    def invalid_email(self):
        locator = Locator(by=By.XPATH, value='//*[@id="center_column"]/div[1]/ol/li')
        return BaseElement(self.driver, locator=locator)

    @property
    def create_account_form(self):
        locator = Locator(by=By.XPATH, value='#account-creation_form > div:nth-child(1) > h3')
        return BaseElement(self.driver, locator=locator)

    # Already registered section
    @property
    def input_email_registered(self):
        locator = Locator(by=By.ID, value='email')
        return BaseElement(self.driver, locator=locator)

    @property
    def input_passwd(self):
        locator = Locator(by=By.ID, value='passwd')
        return BaseElement(self.driver, locator=locator)

    @property
    def btn_forgot_passwd(self):
        locator = Locator(by=By.XPATH, value='//*[@id="login_form"]/div/p[1]/a')
        return BaseElement(self.driver, locator=locator)

    @property
    def btn_sign_in(self):
        locator = Locator(by=By.ID, value='SubmitLogin')
        return BaseElement(self.driver, locator=locator)

    @property
    def authentication_failed(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#center_column > div.alert.alert-danger > ol > li')
        return BaseElement(self.driver, locator=locator)

    @property
    def email_required(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#center_column > div.alert.alert-danger > ol > li')
        return BaseElement(self.driver, locator=locator)

    @property
    def passwd_required(self):
        locator = Locator(by=By.CSS_SELECTOR, value='#center_column > div.alert.alert-danger > ol > li')
        return BaseElement(self.driver, locator=locator)


