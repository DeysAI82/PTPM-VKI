
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://www.globalsqa.com/angularJs-protractor/SimpleCalculator/"

    _FIRST_NUMBER = (By.XPATH, "//input[@ng-model='a']")
    _SECOND_NUMBER = (By.XPATH, "//input[@ng-model='b']")
    _OPERATION = (By.TAG_NAME, "select")
    _RESULT = (By.CSS_SELECTOR, "b.result")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self._FIRST_NUMBER)
        )
        time.sleep(1)

    def enter_first_number(self, number):
        field = self.driver.find_element(*self._FIRST_NUMBER)
        field.clear()
        field.send_keys(str(number))
        time.sleep(0.7)

    def enter_second_number(self, number):
        field = self.driver.find_element(*self._SECOND_NUMBER)
        field.clear()
        field.send_keys(str(number))
        time.sleep(0.7)

    def select_operation(self, operation):
        element = self.driver.find_element(*self._OPERATION)
        Select(element).select_by_value(operation)
        time.sleep(1)

    def get_result(self):
        time.sleep(0.5)
        return self.driver.find_element(*self._RESULT).text
