import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog = "//button[@class='header-catalog-button header-catalog__btn']"

    catalog_laptop = "//a[@data-id='963']"
    laptop = "//a[@to='/noutbuki/']"

    catalog_smartphone = "//a[@data-id='6209']"
    smartphone = "//a[@to='/smartfony/']"

    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_catalog_laptop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_laptop)))

    def get_laptop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop)))

    def get_catalog_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_smartphone)))

    def get_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphone)))

    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print('Click to Catalog')

    def click_catalog_laptop(self):
        self.get_catalog_laptop().click()
        print('Click to Catalog again')

    def click_laptop(self):
        self.get_laptop().click()
        print('Open catalog with laptop')

    def click_catalog_smartphone(self):
        self.get_catalog_smartphone().click()
        print('Click to Catalog again')

    def click_smartphone(self):
        self.get_smartphone().click()
        print('Open catalog with smartphone')

    # Methods

    def transition_to_laptop(self):
        with allure.step("Transition to Laptop"):
            Logger.add_start_step(method='transition_to_laptop')
            self.click_catalog()
            self.click_catalog_laptop()
            self.click_laptop()
            Logger.add_end_step(url=self.driver.current_url, method='transition_to_laptop')

    def transition_to_phone(self):
        with allure.step("Transition to Phone"):
            Logger.add_start_step(method='transition_to_phone')
            self.click_catalog()
            self.click_catalog_smartphone()
            self.click_smartphone()
            Logger.add_end_step(url=self.driver.current_url, method='transition_to_phone')
