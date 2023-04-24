import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Laptop_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    filter_manufacturers = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[2]/div[3]/div[2]/div/div[1]/label/span[2]"
    button_items = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[1]/button[1]"
    listing_display = "//*[@id='listing-top-bar']/div/div[1]/div/label[2]"
    button_comparison_1 = '//*[@id="catalog-main-container"]/div/div[3]/div/article[7]/div/div[2]/div[2]/button[2]/span'
    button_comparison_2 = '//*[@id="catalog-main-container"]/div/div[3]/div/article[21]/div/div[2]/div[2]/button[3]/span'
    comparison_button = "//*[@id='__layout']/div/header/div[2]/div[2]/div/div[2]/a[1]/div"

    laptop = "//a[@title='Ноутбук Acer Extensa EX215-22-A2DW Black (NX.EG9ER.00B)']"

    # Getters

    def get_filter_manufacturers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_manufacturers)))

    def get_button_items(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_items)))

    def get_listing_display(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.listing_display)))

    def get_button_comparison_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_comparison_1)))

    def get_button_comparison_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_comparison_2)))

    def get_comparison_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comparison_button)))

    def get_laptop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop)))

    # Actions

    def click_filter_manufacturers(self):
        self.get_filter_manufacturers().click()
        print('Click to manufacturers filter')

    def click_button_items(self):
        self.get_button_items().click()
        print('Looking at the selected list')

    def click_listing_display(self):
        self.get_listing_display().click()
        print('Changing the display of the product')

    def click_button_comparison_1(self):
        self.get_button_comparison_1().click()
        print('Choosing the first product for comparison')

    def click_button_comparison_2(self):
        self.get_button_comparison_2().click()
        print('Choosing the second product for comparison')

    def click_comparison_button(self):
        self.get_comparison_button().click()
        print('Click to comparison button')

    def click_laptop(self):
        self.get_laptop().click()
        print('Click to laptop')

    # Methods

    def comparison_laptop(self):
        with allure.step("Comparison laptop"):
            Logger.add_start_step(method='comparison_laptop')
            self.click_filter_manufacturers()
            self.click_button_items()
            self.click_listing_display()
            self.driver.execute_script('window.scrollTo(0,700)')
            self.click_button_comparison_1()
            self.driver.execute_script('window.scrollTo(0,2000)')
            self.click_button_comparison_2()
            self.click_comparison_button()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='comparison_laptop')

    def choosing_laptop_1(self):
        with allure.step("Choosing laptop 1"):
            Logger.add_start_step(method='choosing_laptop')
            self.driver.execute_script('window.scrollTo(0,3000)')
            self.click_laptop()
            Logger.add_end_step(url=self.driver.current_url, method='choosing_laptop')
