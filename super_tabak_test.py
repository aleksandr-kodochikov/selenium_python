import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\stati\\PycharmProjects\\selenium_python\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.supertabak.ru/'
driver.get(base_url)
driver.maximize_window()
action = ActionChains(driver)

"""Проверка покупателя на 18 лет"""

# age_no_18 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/a[2]")))
# age_no_18.click()
# time.sleep(3)
#
# driver.get(base_url)
age_yes_18 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/a[1]")))
age_yes_18.click()
time.sleep(3)

"""Авторизация"""

user_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='USER_LOGIN']")))
user_login.send_keys("pythontest_sel")
print('Input Login')

user_password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='USER_PASSWORD']")))
user_password.send_keys("dhT3m7as9Krf")
print('Input Password')

login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Login']")))
login_button.click()
print('Click Enter Account')

# site_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='sitename']")))
user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='js']/body/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div[1]/form/table/tbody/tr[1]/td")))
value_user_name = user_name.text
assert 'pythontest_sel' in value_user_name
print('Good Login')

"""Выбор категории"""
#
# catalog = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='horizontal-multilevel-menu']/li[2]/a")))
# catalog.click()
# print('Click Catalog')
#
# smoking_pipes = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='js']/body/table/tbody/tr[2]/td[2]/div[2]/div[4]/div[1]/div[2]/div[1]/a")))
# smoking_pipes.click()
# print('Click Smoking Pipes')
#
# """Фильтры"""
#
# filter_price_min = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='arrFilter_P1_MIN']")))
# filter_price_min.send_keys("5000")
# print('Input price min')
#
# filter_price_max = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='arrFilter_P1_MAX']")))
# filter_price_max.send_keys("15000")
# print('Input price max')
#
# filter_brand = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-for='arrFilter_86_329487895']")))
# filter_brand.click()
# print('Select brand')
#
# filter_material = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='kombox-filter']/form/ul/li[7]/div[1]")))
# filter_material.click()
# select_material = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-for='arrFilter_89_2895811748']")))
# select_material.click()
# print('Select material')
#
# filter_mouthpiece = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='kombox-filter']/form/ul/li[8]/div[1]")))
# filter_mouthpiece.click()
# select_mouthpiece = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-for='arrFilter_90_1117058440']")))
# select_mouthpiece.click()
# print('Select mouthpiece')
#
# filter_dlina = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='kombox-filter']/form/ul/li[9]/div[1]")))
# filter_dlina.click()
# select_dlina = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-for='arrFilter_95_4005954217']")))
# select_dlina.click()
# print('Select dlina')
#
# filter_handmade = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='kombox-filter']/form/ul/li[13]/div[1]")))
# filter_handmade.click()
# select_handmade = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-for='arrFilter_92_3157780942']")))
# select_handmade.click()
# print('Select handmade')
#
# filter_country = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='kombox-filter']/form/ul/li[15]/div[1]")))
# filter_country.click()
# select_country = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-for='arrFilter_71_1688512129']")))
# select_country.click()
# print('Select country')
#
# filter_set = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='set_filter']")))
# filter_set.click()
# print('Set filters')
#
# add_to_cart_product_1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bx_1245396150_474230']/div[3]/a")))
# add_to_cart_product_1.click()
# print('Add to cart product 1')
# # time.sleep(3)
#
# cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='short_cart']/a[1]")))
# cart.click()
# print('Enter Cart')

"""Выбор табака sidebar"""

# time.sleep(3)
sidebar_tabak = driver.find_element(By.XPATH, "//*[@id='sidebarNavigation']/ul/li[2]/a")
action.move_to_element(sidebar_tabak).perform()

time.sleep(3)
sidebar_tabak_tube = driver.find_element(By.XPATH, "//*[@id='sidebarNavigation']/ul/li[2]/div/ul/li[1]")
action.move_to_element(sidebar_tabak_tube).perform()
# time.sleep(3)
sidebar_tabak_tube.click()
print('Tabak')

slider_low = driver.find_element(By.XPATH, "//*[@id='slider_153']/span[1]")
action.click_and_hold(slider_low).move_by_offset(80, 0).release().perform()
print('Slider left')

filter_slicing = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-for='arrFilter_107_3400593401']")))
filter_slicing.click()
print('Select slicing')

filter_produce = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-for='arrFilter_104_2188530942']")))
filter_produce.click()
print('Select produce')

filter_volume = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-for='arrFilter_108_1462301370']")))
filter_volume.click()
print('Select volume')

filter_set = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='set_filter']")))
filter_set.click()
print('Set filters')

add_to_cart_product_2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bx_1245396150_75802']/div[3]/a/span")))
add_to_cart_product_2.click()
print('Add to cart product 2')

"""Личный кабинет"""

driver.execute_script("window.scrollTo(0, 0)")

personal_account_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Личный кабинет']")))
personal_account_button.click()
print('Personal Account')

main_word = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='js']/body/table/tbody/tr[2]/td[2]/div[2]/div[2]/h1")))
value_main_word = main_word.text
assert value_main_word == 'ЛИЧНЫЙ КАБИНЕТ'
print('Good Personal Account Word')

edit_profile = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='js']/body/table/tbody/tr[2]/td[2]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/a")))
edit_profile.click()
print('Click Edit Profile')

personal_section_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='breadcrumb']/a[2]")))
personal_section_link.click()
print('Click Personal Section')

cart_contain_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='js']/body/table/tbody/tr[2]/td[2]/div[2]/div[2]/div/div[2]/div[1]/ul/li[1]/a")))
cart_contain_button.click()
print('Click Cart Contain')

clear_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='basket_container']/form[2]/a")))
clear_cart.click()
print('Click Clear Cart')

