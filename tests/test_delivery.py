import unittest
from Delivery import calculate_delivery_cost


class TestDelivery(unittest.TestCase):

    def test_minimum_weight(self):
        result = calculate_delivery_cost(0.1, 100, "обычный")
        self.assertEqual(result, (700, "2026-09-04"))

    def test_maximum_weight(self):
        result = calculate_delivery_cost(50.0, 100, "обычный")
        self.assertEqual(result, (1050, "2026-09-04"))

    def test_weight_below_minimum(self):
        result = calculate_delivery_cost(0.09, 100, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_weight_above_maximum(self):
        result = calculate_delivery_cost(50.1, 100, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_distance_below_minimum(self):
        result = calculate_delivery_cost(1.0, 0, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_distance_above_maximum(self):
        result = calculate_delivery_cost(1.0, 5001, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_invalid_package_type(self):
        result = calculate_delivery_cost(1.0, 100, "неизвестный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_fragile_package(self):
        result = calculate_delivery_cost(1.0, 100, "хрупкий")
        self.assertEqual(result, (1000, "2026-09-04"))

    def test_dangerous_package(self):
        result = calculate_delivery_cost(1.0, 100, "опасный")
        self.assertEqual(result, (1700, "2026-09-04"))

    def test_weight_coefficient(self):
        result = calculate_delivery_cost(10.0, 100, "обычный")
        self.assertEqual(result, (840, "2026-09-04"))

    def test_weight_20_kg_coefficient(self):
        result = calculate_delivery_cost(20.0, 100, "обычный")
        self.assertEqual(result, (1050, "2026-09-04"))

    def test_delivery_date_after_500_km(self):
        result = calculate_delivery_cost(1.0, 500, "обычный")
        self.assertEqual(result, (2700, "2026-09-04"))

    def test_express_delivery_should_take_at_least_one_day(self):
        result = calculate_delivery_cost(1.0, 100, "обычный", True)
        self.assertEqual(result[1], "2026-09-04")

    def test_express_delivery_should_not_be_cheaper(self):
        normal = calculate_delivery_cost(1.0, 100, "обычный")
        express = calculate_delivery_cost(1.0, 100, "обычный", True)
        self.assertGreaterEqual(express[0], normal[0])

    def test_weight_5_kg_should_have_weight_coefficient(self):
        result = calculate_delivery_cost(5.0, 100, "обычный")
        self.assertEqual(result[0], 840)


if __name__ == "__main__":
    unittest.main()