import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\stati\\PycharmProjects\\selenium_python\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "locked_out_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_text = warring_text.text
assert value_warring_text == 'Epic sadface: Sorry, this user has been locked out.'
print('Good Test')
time.sleep(3)
driver.refresh()