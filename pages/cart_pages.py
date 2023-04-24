import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    add_to_cart_button = "//button[@data-test-id='add-to-cart-button']"
    button_shopping_cart = "//a[@data-test-id='upsale-to-cart']"
    phone_name = "//*[@id='__layout']/div/div[2]/div/div/div[1]/span/div[1]/div[2]/div/div/div[1]/div/a"
    laptop_name = "//*[@id='__layout']/div/div[2]/div/div/div[1]/span/div[1]/div[2]/div/div/div[1]/div/a"

    # Getters

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_shopping_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_shopping_cart)))

    def get_phone_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_name)))

    def get_laptop_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop_name)))

    # Actions

    def click_button_cart(self):
        self.get_add_to_cart_button().click()
        print('Click to button cart')

    def click_shopping_cart(self):
        self.get_shopping_cart().click()
        print('Go to cart')

    # Methods

    def cart_smartphone(self):
        with allure.step("Cart Smartphone"):
            Logger.add_start_step(method='cart_smartphone')
            self.click_button_cart()
            self.click_shopping_cart()
            self.get_screenshot()
            self.assert_word(self.get_phone_name().text, 'Samsung Galaxy M53 5G 256 ГБ зелёный')
            Logger.add_end_step(url=self.driver.current_url, method='cart_smartphone')

    def cart_laptop(self):
        with allure.step("Cart Laptop"):
            Logger.add_start_step(method='cart_laptop')
            self.click_button_cart()
            self.click_shopping_cart()
            self.get_screenshot()
            self.assert_word(self.get_laptop_name().text, 'Acer Extensa EX215-22-A2DW Black (NX.EG9ER.00B)')
            Logger.add_end_step(url=self.driver.current_url, method='cart_laptop')
