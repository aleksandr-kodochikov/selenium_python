import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\stati\\PycharmProjects\\selenium_python\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()

# login_standard_user = "standard_user"
# password_all = "secret_sauce"
time.sleep(3)
action = ActionChains(driver)
double_2_click = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_2_click).perform()

time.sleep(3)
right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click).perform()

time.sleep(3)
right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.move_to_element()
