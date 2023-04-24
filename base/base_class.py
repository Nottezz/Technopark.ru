import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method assert word"""

    def assert_word(self, word, result):
        assert word == result
        print('Name is good')

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(fr'D:\MyProject\Python\Selenium\Technopark.ru\screenshots\{name_screenshot}')
