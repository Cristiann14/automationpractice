from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.locator import Locator
from utils.base_element import BaseElement
from selenium.webdriver.support.ui import Select

from utils.base_page import BasePage


class CreateAccountPage(BasePage):
    @property
    def get_client_title_mr(self):
        locator = Locator(by=By.ID, value='uniform-id_gender1')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_client_title_mrs(self):
        locator = Locator(by=By.ID, value='uniform-id_gender2')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_client_first_name(self):
        locator = Locator(by=By.ID, value='customer_firstname')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_client_lastName(self):
        locator = Locator(by=By.ID, value='customer_lastname')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_client_email(self):
        locator = Locator(by=By.ID, value='email')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_client_passwd(self):
        locator = Locator(by=By.ID, value='passwd')
        return BaseElement(self.driver, locator=locator)

# BIRTH DAY ELEMENTS
    @property
    def dropdown_birth_day(self):
        locator = Locator(By.ID, value='days')
        return BaseElement(self.driver, locator=locator)

    @property
    def dropdown_birth_month(self):
        locator = Locator(By.ID, value='months')
        return BaseElement(self.driver, locator=locator)

    @property
    def dropdown_birth_year(self):
        locator = Locator(By.ID, value='years')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_firstName_field(self):
        locator = Locator(by=By.ID, value='firstname')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_last_name_field(self):
        locator = Locator(by=By.ID, value='email')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_company_field(self):
        locator = Locator(by=By.ID, value='company')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_address_field(self):
        locator = Locator(by=By.ID, value='address1')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_address_second_field(self):
        locator = Locator(by=By.ID, value='address2')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_city_field(self):
        locator = Locator(by=By.ID, value='city')
        return BaseElement(self.driver, locator=locator)

    @property
    def dropdown_state_field(self):
        locator = Locator(by=By.ID, value='id_state')
        return BaseElement(self.driver, locator=locator)

##### STATE DROPWDOWN SELECTORS ###############
    @property
    def get_postalcode_field(self):
        locator = Locator(by=By.ID, value='postcode')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_additionalinfo_field(self):
        locator = Locator(by=By.ID, value='other')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_homephone_field(self):
        locator = Locator(by=By.ID, value='phone')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_mobilephone_field(self):
        locator = Locator(by=By.ID, value='phone_mobile')
        return BaseElement(self.driver, locator=locator)

    @property
    def get_address_alias_field(self):
        locator = Locator(by=By.ID, value='alias')
        return BaseElement(self.driver, locator=locator)

    @property
    def btn_register(self):
        locator = Locator(by=By.ID, value='submitAccount')
        return BaseElement(self.driver, locator=locator)

# ERRORS
    @property
    def invalid_form(self):
        locator = Locator(by=By.XPATH, value='//*[@id="center_column"]/div/p')
        return BaseElement(self.driver, locator=locator)

    @property
    def email_is_required(self):
        locator = Locator(by=By.XPATH, value='//*[@id="center_column"]/div/p')
        return BaseElement(self.driver, locator=locator)

    @property
    def city_is_required(self):
        locator = Locator(by=By.XPATH, value='//*[@id="center_column"]/div/ol/li[2]/b')
        return BaseElement(self.driver, locator=locator)

    @property
    def postalcode_is_required(self):
        locator = Locator(by=By.XPATH, value='//*[@id="center_column"]/div/ol/li')
        return BaseElement(self.driver, locator=locator)


