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
from pages.create_account_page import CreateAccountPage
from pages.address_page import AddressPage
from selenium.common.exceptions import NoSuchElementException
from pages.shipping_page import ShippingPage
from selenium.webdriver.common.alert import Alert
from pages.payment_page import PaymentPage


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
        self.sign_page.input_email_create.input_text(email)
        self.sign_page.btn_submit_create.click()

        # initiate create_account_page (form page)
        self.create_account_page = CreateAccountPage(driver=self.driver)

        # YOUR PERSONAL INFORMATION
        self.create_account_page.get_client_title_mr.click()
        self.create_account_page.get_client_first_name.input_text('John')
        self.create_account_page.get_client_lastName.input_text('John')
        # email row pre-filled
        self.create_account_page.get_client_passwd.input_text('123467')
        # date of bird

        # YOUR ADDRESS
        # self.create_account_page.get_firstName_field.input_text('John')
        # self.create_account_page.get_last_name_field.input_text('John')
        self.create_account_page.get_company_field.input_text('Company')
        self.create_account_page.get_address_field.input_text('Address')
        self.create_account_page.get_city_field.input_text('City')
        # state
        self.create_account_page.dropdown_state_field.option('Alabama')
        self.create_account_page.get_postalcode_field.input_text('10000')
        # country
        self.create_account_page.get_homephone_field.input_text('070000122')
        self.create_account_page.get_mobilephone_field.input_text('0700000000')
        self.create_account_page.get_address_alias_field.input_text('Address')

        self.create_account_page.btn_register.click()

        self.address_page = AddressPage(driver=self.driver)
        self.address_page.btn_submit.click()

        self.shipping_page = ShippingPage(driver=self.driver)

    def test1_not_agree_terms(self):
        self.shipping_page.btn_submit.click()
        assert self.shipping_page.uncheked_terms.text == 'You must agree to the terms of service before continuing.'

    def test2_btn_continue_shopping(self):
        self.shipping_page.btn_continue_shopping.click()
        assert self.shipping_page.get_url == 'http://automationpractice.com/index.php?controller=order&step=1&multi-shipping=', 'Wrong page displayed'

    def test3_btn_proceed_to_checkout(self):
        self.shipping_page.checkbox_terms.click()
        self.shipping_page.btn_submit.click()
        self.payment_page = PaymentPage(driver=self.driver)
        assert self.payment_page.page_heading == 'Please choose your payment method'


if __name__ == '__main__':
    unittest.main()
