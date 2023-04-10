import time
import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\stati\\PycharmProjects\\selenium_python\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

"""Очищаем поле Date Picker"""
time.sleep(2)
new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.send_keys(Keys.BACKSPACE*10)
new_date.click()
time.sleep(2)

"""Получаем текущую дату и прибавляем 10 дней"""
current_date = datetime.date.today()
current_date_str = current_date.strftime('%m/%d/%Y')
print('Текущая дата: ', current_date_str)
future_date = datetime.date.today() + datetime.timedelta(days=10)
future_date_string = future_date.strftime('%m/%d/%Y')
print('Новая дата: ', future_date_string)

"""Вводим новую дату"""
new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.send_keys(future_date_string)
new_date.click()




