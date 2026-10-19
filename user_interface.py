
from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def get_data(self):
        pass


class ConsoleInterface(UserInterface):
    def get_data(self):
        weight = float(input("Введите вес посылки: "))
        distance = int(input("Введите расстояние доставки: "))
        package_type = input(
            "Тип посылки (обычный, хрупкий, опасный): "
        )
        is_express = input(
            "Экспресс-доставка? (да/нет): "
        ).lower() == "да"

        return weight, distance, package_type, is_express
