import unittest
import random
import string

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.locator import Locator
from utils.base_element import BaseElement
from pages.summary_page import SummaryPage
from utils.base_page import BasePage
from pages.sign_page import SignPage
from pages.address_page import AddressPage

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # create new Chrome session
        self.driver = webdriver.Chrome("C:/Users/cristian.prepelita/projects/drivers/chromedriver.exe")
        url = 'http://automationpractice.com/index.php'
        # navigate to the application cart
        self.driver.get(url)

        # add product to cart
        product = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]')
        product.click()

        self.driver.implicitly_wait(7)
        checkout = self.driver.find_element_by_css_selector("a[title='Proceed to checkout']")
        checkout.click()

        self.summary_page = SummaryPage(driver=self.driver)
        self.summary_page.btn_proceed_to_checkout.click()

        self.sign_page = SignPage(driver=self.driver)

# ALREADY REGISTERED SECTION
    def test1_sign_in_invalid_credits(self):
        # insert unregistered credits
        self.sign_page.input_email_registered.input_text('asd@ads.com')
        self.sign_page.input_passwd.input_text('1234')
        self.sign_page.btn_sign_in.click()
        assert self.sign_page.authentication_failed.text == 'Authentication failed.', 'Authentication failed wrong alert'

    def test2_forgot_password_btn(self):
        self.sign_page.btn_forgot_passwd.click()
        assert 'Forgot your password - My Store' in self.driver.title , 'Wrong page displayed'

    def test3_empty_email_field(self):
        self.sign_page.input_passwd.input_text('1234')
        self.sign_page.btn_sign_in.click()
        assert self.sign_page.email_required.text == 'An email address required.'

    def test4_empty_passwd_field(self):
        self.sign_page.input_email_registered.input_text('asd@ad.ro')
        self.sign_page.btn_sign_in.click()
        assert self.sign_page.passwd_required.text == 'Password is required.'

    def test5_invalid_email_field(self):
        self.sign_page.input_email_registered.input_text('1234')
        assert self.sign_page.invalid_email.text == 'Invalid email address.'

    def test6_sign_in_valid_account(self):
        self.sign_page.input_email_registered.input_text('asdas@asffd.a')
        self.sign_page.input_passwd.input_text('aaaaa')
        self.sign_page.btn_sign_in.click()

        self.address_page = AddressPage(driver=self.driver)
        assert self.address_page.page_heading.text == 'Addresses', 'Wrong page displayed'

# CREATE AN ACCOUNT SECTION
    def test6_insert_valid_email(self):
        name = random.choice(string.ascii_letters)
        address = random.choice(string.ascii_letters)
        domain = random.choice(string.ascii_letters)
        email = name + '@' + address + '.' + domain
        self.sign_page.input_email_create.input_text(email)
        self.sign_page.btn_submit_create.click()
        assert self.sign_page.create_account_form.text == 'Your personal information'

    def test7_insert_invalid_email(self):
        self.sign_page.input_email_create.input_text('asd')
        self.sign_page.btn_submit_create.click()
        assert self.sign_page.invalid_email.text == 'Invalid email address.'


if __name__ == '__main__':
    unittest.main()
