import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.locator import Locator
from utils.base_element import BaseElement
from pages.summary_page import SummaryPage
from utils.base_page import BasePage


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

        # go to the cart page
        checkout = self.driver.find_element_by_css_selector("a[title='Proceed to checkout']")
        checkout.click()

        # initiate summary page
        self.summary_page = SummaryPage(driver=self.driver)

    def test1_increase_qty_of_product(self):
        self.summary_page.btn_add_qty.click()
        self.driver.implicitly_wait('4')
        assert self.summary_page.total_price_products.text == '$33.02', 'Wrong price displayed'
        assert self.summary_page.final_price_products.text == '$35.02', 'Wrong final price displayed'

    def test2_decrease_qty_of_product(self):
        self.summary_page.btn_remove_qty.click()
        #assert self.summary_page.total_price_products.text == '$16.51', 'Wrong price displayed'
        assert self.summary_page.empty_cart_alert.text == 'Your shopping cart is empty.', 'Cart error'

    def test3_delete_from_cart(self):
        self.summary_page.btn_remove_qty.click()
        assert self.summary_page.empty_cart_alert.text == 'Your shopping cart is empty.', 'Cart error'

    def test4_btn_proceed_to_checkout(self):
        self.summary_page.btn_proceed_to_checkout.click()
        assert self.driver.title == 'Login - My Store', 'Wrong page displayed'


if __name__ == '__main__':
    unittest.main()
