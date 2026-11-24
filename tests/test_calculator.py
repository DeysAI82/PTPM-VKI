import unittest
import os

from selenium import webdriver
from pages.calculator_page import CalculatorPage


class TestCalculator(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.page = CalculatorPage(self.driver)
        self.page.open()

    def tearDown(self):
        os.makedirs("screenshots", exist_ok=True)

        self.driver.save_screenshot(
            os.path.join("screenshots", self._testMethodName + ".png")
        )

        self.driver.quit()

    def calculate(self, first, second, operation):
        self.page.enter_first_number(first)
        self.page.enter_second_number(second)
        self.page.select_operation(operation)

        return self.page.get_result()

    def test_addition(self):
        result = self.calculate(2, 3, "+")
        self.assertIn("5", result)

    def test_subtraction(self):
        result = self.calculate(5, 3, "-")
        self.assertIn("2", result)

    def test_multiplication(self):
        result = self.calculate(4, 3, "*")
        self.assertIn("12", result)

    def test_division(self):
        result = self.calculate(10, 2, "/")
        self.assertIn("5", result)

    def test_zero(self):
        result = self.calculate(0, 5, "+")
        self.assertIn("0", result)

    def test_negative_numbers(self):
        result = self.calculate(-5, 3, "+")
        self.assertIn("-2", result)


if __name__ == "__main__":
    unittest.main()
