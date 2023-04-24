import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import undetected_chromedriver as uc

from pages.cart_pages import Cart_page
from pages.catalog_pages import Catalog_page
from pages.laptop_pages import Laptop_page
from pages.main_pages import Main_page


@allure.description("Test comparison Laptop")
def test_comparison_laptop():

    # s = Service(executable_path='path_to_chromedriver')
    # driver = webdriver.Chrome(service=s)
    # driver.get('https://www.technopark.ru')

    driver = uc.Chrome()
    driver.get('https://www.technopark.ru')

    print('Start Test')

    mp = Main_page(driver)
    mp.open_page()

    cp = Catalog_page(driver)
    cp.transition_to_laptop()

    lp = Laptop_page(driver)
    lp.comparison_laptop()

    driver.close()

    print('Finish Test')

@allure.description("Test buy Laptop")
def test_buy_laptop():

    # s = Service(executable_path='path_to_chromedriver')
    # driver = webdriver.Chrome(service=s)
    # driver.get('https://www.technopark.ru')

    driver = uc.Chrome()
    driver.get('https://www.technopark.ru')

    print('Start Test')

    mp = Main_page(driver)
    mp.open_page()

    cp = Catalog_page(driver)
    cp.transition_to_laptop()

    lp = Laptop_page(driver)
    lp.choosing_laptop_1()

    cr = Cart_page(driver)
    cr.cart_laptop()

    print('Finish Test')
