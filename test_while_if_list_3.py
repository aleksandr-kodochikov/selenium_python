
print('Добро пожаловать в наш интернет-магазин!')
product = []
locator_product_1 = ["//a[@id='item_4_title_link']", "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-backpack']"]
locator_product_2 = ["//a[@id='item_0_title_link']", "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-bike-light']"]
locator_product_3 = ["//a[@id='item_1_title_link']", "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"]
locator_product_4 = ["//a[@id='item_5_title_link']", "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"]
locator_product_5 = ["//a[@id='item_2_title_link']", "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div", "//button[@id='add-to-cart-sauce-labs-onesie']"]
locator_product_6 = ["//a[@id='item_3_title_link']", "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div", "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"]

while True:
    n = input("""Для выбора одного из следующих товаров, укажите его номер:
1 - Sauce Labs Backpack
2 - Sauce Labs Bike Light
3 - Sauce Labs Bolt T-Shirt
4 - Sauce Labs Fleece Jacket
5 - Sauce Labs Onesie
6 - Test.allTheThings() T-Shirt (Red)\n""")
    if n == '1':
        product = locator_product_1
        break
    elif n == '2':
        product = locator_product_2
        break
    elif n == '3':
        product = locator_product_3
        break
    elif n == '4':
        product = locator_product_4
        break
    elif n == '5':
        product = locator_product_5
        break
    elif n == '6':
        product = locator_product_6
        break
    else:
        print('Неверный номер товара!')

print(product[0])
print(product[1])
print(product[2])