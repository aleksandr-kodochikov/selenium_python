

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# g = Service('C:\\Users\\stati\\PycharmProjects\\selenium_python\\chromedriver.exe')
# driver = webdriver.Chrome(options=options, service=g)
# base_url = 'https://www.saucedemo.com/'
# driver.get(base_url)
# driver.maximize_window()
#
# login_standard_user = "standard_user"
# password_all = "secret_sauce"
#
# user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# user_name.send_keys(login_standard_user)
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
#
# url = 'https://www.saucedemo.com/inventory.html'
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print('Good URL')

str_1 = 'Item total: $57.980000000000004'
# str_2 = '$7.99'
# dig_str_2 = str_2[1:]
dig_str_1 = str_1[13:]
# total = float(dig_str_1) + float(dig_str_2)
print(dig_str_1)
# print(dig_str_2)
# print(total)