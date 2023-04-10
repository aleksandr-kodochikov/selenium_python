import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\stati\\PycharmProjects\\selenium_python\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

# login_standard_user = "standard_user"
# password_all = "secret_sauce"
time.sleep(3)
# check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
# check_box.click()
# time.sleep(3)
# check_box_1 = driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]")
# check_box_1.click()
#
# time.sleep(3)
# check_box_2 = driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]")
# check_box_2.click()
#
# time.sleep(3)
# check_box_3 = driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]")
# check_box_3.click()

radio_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
radio_button.click()
