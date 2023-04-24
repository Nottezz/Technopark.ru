import allure

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    url = 'https://www.technopark.ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    # Getters


    # Actions


    # Methods

    def open_page(self):
        with allure.step("Open Main page"):
            Logger.add_start_step(method='open_page')
            self.driver.get(self.url)
            self.driver.maximize_window()
            Logger.add_end_step(url=self.driver.current_url, method='open_page')
