import unittest
from main import triangle


class TestTriangle(unittest.TestCase):

    def test_equilateral_triangle(self):
        result = triangle("3", "3", "3")
        self.assertEqual(result[0], "равносторонний")

    def test_isosceles_triangle(self):
        result = triangle("3", "3", "4")
        self.assertEqual(result[0], "равнобедренный")

    def test_scalene_triangle(self):
        result = triangle("3", "4", "5")
        self.assertEqual(result[0], "разносторонний")

    def test_invalid_triangle_by_sides(self):
        result = triangle("1", "2", "10")
        self.assertEqual(result[0], "не треугольник")
        self.assertEqual(result[1], [(-1, -1)] * 3)

    def test_negative_side(self):
        result = triangle("-3", "4", "5")
        self.assertEqual(result[0], "не треугольник")
        self.assertEqual(result[1], [(-1, -1)] * 3)

    def test_zero_side(self):
        result = triangle("0", "4", "5")
        self.assertEqual(result[0], "не треугольник")
        self.assertEqual(result[1], [(-1, -1)] * 3)

    def test_non_numeric_first_side(self):
        result = triangle("abc", "4", "5")
        self.assertEqual(result[0], "")
        self.assertEqual(result[1], [(-2, -2)] * 3)

    def test_non_numeric_second_side(self):
        result = triangle("3", "abc", "5")
        self.assertEqual(result[0], "")
        self.assertEqual(result[1], [(-2, -2)] * 3)

    def test_non_numeric_third_side(self):
        result = triangle("3", "4", "abc")
        self.assertEqual(result[0], "")
        self.assertEqual(result[1], [(-2, -2)] * 3)

    def test_coordinates_are_in_range(self):
        result = triangle("3", "4", "5")

        for x, y in result[1]:
            self.assertGreaterEqual(x, 0)
            self.assertLessEqual(x, 100)
            self.assertGreaterEqual(y, 0)
            self.assertLessEqual(y, 100)


if __name__ == "__main__":
    unittest.main()