import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import undetected_chromedriver as uc

from pages.main_pages import Main_page
from pages.catalog_pages import Catalog_page
from pages.smartphone_pages import Smartphone_page
from pages.laptop_pages import Laptop_page
from pages.cart_pages import Cart_page


@allure.description("Test buy Smartphone")
def test_buy_smartphone():

    # s = Service(executable_path='path_to_chromedriver')
    # driver = webdriver.Chrome(service=s)
    # options = webdriver.ChromeOptions
    #
    # options.add_argument('--user-data-dir=./User_data')
    # options.add_argument('--profile-directory=./User_data/Profile_1')
    #
    # driver.get('https://www.technopark.ru')

    driver = uc.Chrome()
    driver.get('https://www.technopark.ru')

    print('Start Test')

    mp = Main_page(driver)
    mp.open_page()

    cp = Catalog_page(driver)
    cp.transition_to_phone()

    sp = Smartphone_page(driver)
    sp.choosing_smartphone_1()

    cr = Cart_page(driver)
    cr.cart_smartphone()

    # driver.close()
    print('Finish Test')


