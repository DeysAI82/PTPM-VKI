import unittest
from unittest.mock import Mock, patch

from triangle_calculator import TriangleCalculator
from triangle_database import Database
from triangle_user_interface import ConsoleInterface
from triangle_external_service import MockExternalService
from triangle_controller import TriangleController


class TestLab3Triangle(unittest.TestCase):
    def setUp(self):
        self.calculator = TriangleCalculator()
        self.database = Database()
        self.user_interface = Mock()
        self.external_service = Mock()

        self.controller = TriangleController(
            self.calculator,
            self.database,
            self.user_interface,
            self.external_service
        )

    def tearDown(self):
        self.database.close()

    def test_database_add_and_get(self):
        self.database.add(3, 4, 5, "разносторонний", "")

        result = self.database.get(3, 4, 5)

        self.assertEqual(result, ("разносторонний", ""))

    def test_database_delete(self):
        self.database.add(3, 4, 5, "разносторонний", "")
        self.database.delete(3, 4, 5)

        self.assertIsNone(self.database.get(3, 4, 5))

    def test_controller_calculates_and_saves(self):
        self.user_interface.get_data.return_value = ("3", "4", "5")

        result = self.controller.run()
        saved = self.database.get("3", "4", "5")

        self.assertEqual(result[0], "разносторонний")
        self.assertEqual(saved, ("разносторонний", ""))

    def test_controller_uses_saved_result(self):
        self.database.add(3, 4, 5, "разносторонний", "")
        self.user_interface.get_data.return_value = (3, 4, 5)

        calculator = Mock()
        controller = TriangleController(
            calculator,
            self.database,
            self.user_interface,
            self.external_service
        )

        result = controller.run()

        calculator.calculate.assert_not_called()
        self.assertEqual(result[0], "разносторонний")

    @patch("builtins.input", side_effect=["3", "4", "5"])
    def test_controller_gets_user_input(self, mock_input):
        interface = ConsoleInterface()
        controller = TriangleController(
            self.calculator,
            self.database,
            interface,
            self.external_service
        )

        result = controller.run()

        self.assertEqual(result[0], "разносторонний")
        self.assertEqual(mock_input.call_count, 3)

    def test_controller_sends_result(self):
        self.user_interface.get_data.return_value = ("3", "4", "5")

        self.controller.run()

        self.external_service.send.assert_called_once_with(
            "Тип треугольника: разносторонний"
        )

    def test_controller_handles_invalid_triangle(self):
        self.user_interface.get_data.return_value = ("1", "2", "10")

        result = self.controller.run()

        self.assertEqual(result[0], "не треугольник")
        self.assertTrue(result[1])
        self.external_service.send.assert_called_once_with(
            "Треугольник с такими сторонами не существует"
        )


if __name__ == "__main__":
    unittest.main()