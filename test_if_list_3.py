
print('Добро пожаловать в наш интернет-магазин!\n', 'Для выбора одного из следующих товаров, укажите его номер:', sep='')
print('1 - Sauce Labs Backpack')
print('2 - Sauce Labs Bike Light')
print('3 - Sauce Labs Bolt T-Shirt')
print('4 - Sauce Labs Fleece Jacket')
print('5 - Sauce Labs Onesie')
print('6 - Test.allTheThings() T-Shirt (Red)')
n = int(input())
product = []
locator_product_1 = ["//a[@id='item_4_title_link']", "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-backpack']"]
locator_product_2 = ["//a[@id='item_0_title_link']", "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-bike-light']"]
locator_product_3 = ["//a[@id='item_1_title_link']", "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"]
locator_product_4 = ["//a[@id='item_5_title_link']", "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"]
locator_product_5 = ["//a[@id='item_2_title_link']", "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-onesie']"]
locator_product_6 = ["//a[@id='item_3_title_link']", "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div", "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"]

if n == 1: product = locator_product_1
if n == 2: product = locator_product_2
if n == 3: product = locator_product_3
if n == 4: product = locator_product_4
if n == 5: product = locator_product_5
if n == 6: product = locator_product_6

print(product[0])
print(product[1])
print(product[2])