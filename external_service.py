
from abc import ABC, abstractmethod


class ExternalService(ABC):
    @abstractmethod
    def send(self, message):
        pass


class MockExternalService(ExternalService):
    def send(self, message):
        print("Отправка результата:", message)
        return True
