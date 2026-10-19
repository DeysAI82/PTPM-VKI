
import unittest
from unittest.mock import Mock, patch

from database import Database
from user_interface import ConsoleInterface
from external_service import MockExternalService
from controller import Controller


class TestLab3(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.user_interface = Mock()
        self.external_service = Mock()
        self.controller = Controller(
            self.database,
            self.user_interface,
            self.external_service
        )

    def tearDown(self):
        self.database.close()

    def test_database_add_and_get(self):
        self.database.add(1, 100, "обычный", False, 700, "2026-09-04")
        result = self.database.get(1, 100, "обычный", False)

        self.assertEqual(result, (700, "2026-09-04"))

    def test_database_delete(self):
        self.database.add(1, 100, "обычный", False, 700, "2026-09-04")
        self.database.delete(1, 100, "обычный", False)

        result = self.database.get(1, 100, "обычный", False)

        self.assertIsNone(result)

    def test_controller_calculates_and_saves(self):
        self.user_interface.get_data.return_value = (
            1, 100, "обычный", False
        )

        result = self.controller.run()
        saved = self.database.get(1, 100, "обычный", False)

        self.assertEqual(result[0], 700)
        self.assertEqual(saved, (700, "2026-09-04"))

    @patch("controller.calculate_delivery_cost")
    def test_controller_uses_saved_result(self, mock_calculate):
        self.database.add(1, 100, "обычный", False, 700, "2026-09-04")
        self.user_interface.get_data.return_value = (
            1, 100, "обычный", False
        )

        result = self.controller.run()

        mock_calculate.assert_not_called()
        self.assertEqual(result[0], 700)

    @patch("builtins.input", side_effect=["1", "100", "обычный", "нет"])
    def test_controller_gets_user_input(self, mock_input):
        interface = ConsoleInterface()
        controller = Controller(
            self.database, interface, self.external_service
        )

        result = controller.run()

        self.assertEqual(result[0], 700)
        self.assertEqual(mock_input.call_count, 4)

    def test_controller_sends_result(self):
        self.user_interface.get_data.return_value = (
            1, 100, "обычный", False
        )

        self.controller.run()

        self.external_service.send.assert_called_once_with(
            "Стоимость доставки: 700 руб. Дата доставки: 2026-09-04"
        )

    def test_controller_handles_invalid_data(self):
        self.user_interface.get_data.return_value = (
            1, 100, "неизвестный", False
        )

        result = self.controller.run()

        self.assertEqual(result[0], -1)
        self.external_service.send.assert_called_once_with(
            "Некорректные параметры доставки"
        )


if __name__ == "__main__":
    unittest.main()
