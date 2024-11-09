from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def process(self, file):
        pass