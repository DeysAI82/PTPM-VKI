from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def get_data(self):
        pass


class ConsoleInterface(UserInterface):
    def get_data(self):
        a = input("Введите сторону A: ")
        b = input("Введите сторону B: ")
        c = input("Введите сторону C: ")

        return a, b, c