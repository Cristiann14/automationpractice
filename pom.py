from datetime import time
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.summary_page import SummaryPage
from pages.summary_page import SummaryPage


# ----BROWSER SETUP----
browser = webdriver.Chrome("C:/Users/cristian.prepelita/projects/drivers/chromedriver.exe")
#url = 'http://automationpractice.com/index.php?id_product=1&controller=product'
url = 'http://automationpractice.com/index.php'


# ADD PRODUCT TO CART
browser.get(url)
product = browser.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]')
product.click()


# WAIT PRODUCT TO BE ADDED
browser.implicitly_wait(7)

# GO TO CART PAGE ( SUMMARY TAB )
checkout = browser.find_element_by_css_selector("a[title='Proceed to checkout']")
checkout.click()


# SUMMARY PAGE TEST
summary_page = SummaryPage(driver=browser)

#summary_page.btn_add_qty.click()
summary_page.btn_remove_qty.click()
browser.implicitly_wait('4')
print(summary_page.empty_cart_alert.text)


# delete cart product
#summary_page.btn_remove_qty.click()
#assert summary_page.empty_cart_alert.text == 'Your shopping cart is emptya.' , 'Wrong'



#summary_page.input_qty.input_text('10')

    #summaryPage


#check if cart is empty

#assert summary_page.text_cart_is_empty.text == 'Your shopping cart is empty.', "Test passed"

#browser.quit()