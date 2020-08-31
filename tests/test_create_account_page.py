import unittest
import random
import string

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.locator import Locator
from selenium.webdriver.support import expected_conditions as EC
from utils.base_element import BaseElement
from pages.summary_page import SummaryPage
from utils.base_page import BasePage
from pages.sign_page import SignPage
from pages.create_account_page import CreateAccountPage
from pages.address_page import AddressPage
name = random.choice(string.ascii_letters)
address = random.choice(string.ascii_letters)
domain = random.choice(string.ascii_letters)
email2 = name + '@' + address + '.' + domain

class MyTestCase(unittest.TestCase):

    def setUp(self):
        global email2
        # create new Chrome session
        self.driver = webdriver.Chrome("C:/Users/cristian.prepelita/projects/drivers/chromedriver.exe")
        url = 'http://automationpractice.com/index.php'

        # navigate to the application cart
        self.driver.get(url)

        # add product to cart
        product = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]')
        product.click()

        self.driver.implicitly_wait(7)
        # go to cart
        checkout = self.driver.find_element_by_css_selector("a[title='Proceed to checkout']")
        checkout.click()

        # initiate summary page
        self.summary_page = SummaryPage(driver=self.driver)
        # proceed to the next step
        self.summary_page.btn_proceed_to_checkout.click()

        # initiate sign page
        self.sign_page = SignPage(driver=self.driver)

        # generate valid email
        name = random.choice(string.ascii_letters)
        address = random.choice(string.ascii_letters)
        domain = random.choice(string.ascii_letters)
        email = name + '@' + address + '.' + domain
        # insert the email and submit the button
        self.sign_page.input_email_create.input_text(email2)
        self.sign_page.btn_submit_create.click()

        #initiate create_account_page (form page)
        self.create_account_page = CreateAccountPage(driver=self.driver)

    def test1_submit_empty_form(self):
        self.create_account_page.btn_register.click()
        assert self.create_account_page.invalid_form.text == 'There are 8 errors', 'Wrong error message generated'

    def test2_submit_valid_form(self):
        # YOUR PERSONAL INFORMATION
        self.create_account_page.get_client_title_mr.click()
        self.create_account_page.get_client_first_name.input_text('John')
        self.create_account_page.get_client_lastName.input_text('John')
        #email row pre-filled
        self.create_account_page.get_client_passwd.input_text('12345')

        # date of bird

        # YOUR ADDRESS
        #self.create_account_page.get_firstName_field.input_text('John')
        #self.create_account_page.get_last_name_field.input_text('John')
        self.create_account_page.get_company_field.input_text('Company')
        self.create_account_page.get_address_field.input_text('Address')
        #self.create_account_page.get_address_second_field.text('Address')
        self.create_account_page.get_city_field.input_text('City')
        #state
        self.create_account_page.dropdown_state_field.option('Alabama')
        self.create_account_page.get_postalcode_field.input_text('10000')
        #country
        self.create_account_page.get_homephone_field.input_text('0700001221')
        self.create_account_page.get_mobilephone_field.input_text('0700000000')
        #self.create_account_page.get_address_alias_field.input_text('Address')

        self.create_account_page.btn_register.click()

        self.address_page = AddressPage(driver=self.driver)

        assert self.address_page.page_heading.text == 'Addresses', 'Wrong page header'

    def test3_invalid_passwd(self):
        self.create_account_page.get_client_passwd.input_text('aa')
        self.create_account_page.btn_register.click()
        if self.create_account_page.email_is_required.text:
            print("Invalid test password passed")
        else:
            print("Error passoword")

    def test4_check_email(self):
        email = self.driver.find_element_by_css_selector('input#email')
        email_value = email.get_attribute("value")
        assert email == email2, 'Different email'

    def test5_city_required(self):
        self.create_account_page.get_city_field.text('')
        self.create_account_page.btn_register.click()
        if self.create_account_page.city_is_required.text:
            print("Invalid test city field passed")
        else:
            prin("Error city field")

    def test6_postalcode_required(self):
        self.create_account_page.get_city_field.text('')
        self.create_account_page.btn_register.click()
        if self.create_account_page.city_is_required.text:
            print("Invalid test postal code field passed")
        else:
            prin("Error postal code field")


if __name__ == '__main__':
    unittest.main()
