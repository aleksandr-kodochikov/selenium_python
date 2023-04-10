

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\stati\\PycharmProjects\\selenium_python\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

# user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
user_name.send_keys(login_standard_user)
print('Input Login')
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input Password')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('Click Login Button')

# locator_product_1 = "//a[@id='item_4_title_link']"
# locator_price_product_1 = "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"
# locator_select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
# locator_cart_price_1 = "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"
# locator_final_product_1 = "//a[@id='item_4_title_link']"
# locator_final_price_1 = "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"
# locator_item_total = "//*[@id='checkout_summary_container']/div/div[2]/div[6]"
#
# """INFO Product #1"""
# product_1 = driver.find_element(By.XPATH, locator_product_1)
# value_product_1 = product_1.text
# print(value_product_1)
#
# price_product_1 = driver.find_element(By.XPATH, locator_price_product_1)
# value_price_product_1 = price_product_1.text
# print(value_price_product_1)
#
# select_product_1 = driver.find_element(By.XPATH, locator_select_product_1)
# select_product_1.click()
# print('Add To Cart Product 1')
#
#
# cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
# cart.click()
# print('Enter Cart')
#
# """INFO Cart Products"""
# cart_product_1 = driver.find_element(By.XPATH, locator_product_1)
# value_cart_product_1 = cart_product_1.text
# print(value_cart_product_1)
# assert value_product_1 == value_cart_product_1
# print('INFO Cart Product 1 Good')
#
# price_cart_product_1 = driver.find_element(By.XPATH, locator_cart_price_1)
# value_price_cart_product_1 = price_cart_product_1.text
# print(value_price_cart_product_1)
# assert value_price_product_1 == value_price_cart_product_1
# print('INFO Cart Price Product 1 Good')
#
#
# button_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
# button_checkout.click()
# print('Click Checkout')
#
# """Select User INFO"""
# first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
# first_name.send_keys('Donald')
# print('Input First Name')
#
# last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
# last_name.send_keys('Trump')
# print('Input Last Name')
#
# zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
# zip.send_keys('453300')
# print('Input ZIP')
#
# button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
# button_continue.click()
# print('Click Continue')
#
# """INFO Final Products"""
# final_product_1 = driver.find_element(By.XPATH, locator_product_1)
# value_final_product_1 = final_product_1.text
# print(value_final_product_1)
# assert value_product_1 == value_final_product_1
# print('INFO Final Product 1 Good')
#
# price_final_product_1 = driver.find_element(By.XPATH, locator_final_price_1)
# value_price_final_product_1 = price_final_product_1.text
# print(value_price_final_product_1)
# assert value_price_product_1 == value_price_final_product_1
# print('INFO Final Price Product 1 Good')
#
#
# summary_price = driver.find_element(By.XPATH, locator_item_total)
# value_summary_price = summary_price.text
# print(value_summary_price)
#
# total_summ = float(value_price_product_1[1:])
# value_total_summ = 'Item total: $' + str(total_summ)
# print(value_total_summ)
# assert value_summary_price == value_total_summ
# print('INFO Item Total Good')




# url = 'https://www.saucedemo.com/inventory.html'
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print('Good URL')