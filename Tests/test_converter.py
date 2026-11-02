
import unittest
from Converter import Converter


class TestConverter(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(Converter.do(65.7), 65)

    def test_upper_boundary(self):
        self.assertEqual(Converter.do(100.7), 1000)

    def test_above_upper_boundary(self):
        self.assertEqual(Converter.do(150.5), 1000)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Converter.do(0.0)

    def test_negative(self):
        self.assertEqual(Converter.do(-12.7), -17)

    def test_lower_boundary(self):
        self.assertEqual(Converter.do(-30.4), -35)

    def test_below_lower_boundary(self):
        self.assertEqual(Converter.do(-30.5), -2000)

    def test_large_negative(self):
        self.assertEqual(Converter.do(-94.5), -2000)


if __name__ == "__main__":
    unittest.main()
