import logging
import sys
import os
import math
import unittest


os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | [%(levelname)-7s] | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/file_txt.log", encoding="utf-8")
    ]

)


def triangle(a, b, c):
    logging.info(f"Получены стороны: A={a}, B={b}, C={c}")

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        logging.error("Введены нечисловые данные")
        return "", [(-2, -2)] * 3

    if a <= 0 or b <= 0 or c <= 0:
        logging.warning("Стороны должны быть положительными")
        return "не треугольник", [(-1, -1)] * 3

    if a + b <= c or a + c <= b or b + c <= a:
        logging.warning("Треугольник с такими сторонами не существует")
        return "не треугольник", [(-1, -1)] * 3

    if a == b == c:
        kind = "равносторонний"
    elif a == b or a == c or b == c:
        kind = "равнобедренный"
    else:
        kind = "разносторонний"

    x1 = 0
    y1 = 0
    x2 = a
    y2 = 0

    x3 = (a * a + b * b - c * c) / (2 * a)
    y3 = math.sqrt(b * b - x3 * x3)

    max_x = max(x1, x2, x3)
    max_y = max(y1, y2, y3)

    scale = min(90 / max_x, 90 / max_y)

    coordinates = [
        (round(x1 * scale + 5), round(y1 * scale + 5)),
        (round(x2 * scale + 5), round(y2 * scale + 5)),
        (round(x3 * scale + 5), round(y3 * scale + 5))
    ]

    logging.info(f"Тип треугольника: {kind}")
    logging.info(f"Координаты: {coordinates}")
    logging.info("Запрос успешно обработан")

    return kind, coordinates


class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        result = triangle("3", "3", "3")
        self.assertEqual(result[0], "равносторонний")

    def test_isosceles(self):
        result = triangle("3", "3", "4")
        self.assertEqual(result[0], "равнобедренный")

    def test_scalene(self):
        result = triangle("3", "4", "5")
        self.assertEqual(result[0], "разносторонний")

    def test_not_triangle(self):
        result = triangle("1", "2", "10")
        self.assertEqual(result[0], "не треугольник")
        self.assertEqual(result[1], [(-1, -1)] * 3)

    def test_negative(self):
        result = triangle("-3", "4", "5")
        self.assertEqual(result[0], "не треугольник")
        self.assertEqual(result[1], [(-1, -1)] * 3)

    def test_zero(self):
        result = triangle("0", "4", "5")
        self.assertEqual(result[0], "не треугольник")
        self.assertEqual(result[1], [(-1, -1)] * 3)

    def test_not_number(self):
        result = triangle("abc", "4", "5")
        self.assertEqual(result[0], "")
        self.assertEqual(result[1], [(-2, -2)] * 3)

    def test_coordinates(self):
        result = triangle("3", "4", "5")

        for x, y in result[1]:
            self.assertGreaterEqual(x, 0)
            self.assertLessEqual(x, 100)
            self.assertGreaterEqual(y, 0)
            self.assertLessEqual(y, 100)


if __name__ == "__main__":
    print("1 - Запустить программу")
    print("2 - Запустить тесты")

    choice = input("Выберите действие: ")

    if choice == "1":
        a = input("Введите сторону A: ")
        b = input("Введите сторону B: ")
        c = input("Введите сторону C: ")

        kind, coordinates = triangle(a, b, c)

        print()
        print("Тип треугольника:", kind)
        print("Координаты:", coordinates)

    elif choice == "2":
        unittest.main()