from abc import ABC, abstractmethod


class CarRepository(ABC):
    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def find_by_brand(self, brand): pass

    @abstractmethod
    def get_min_price(self): pass

    @abstractmethod
    def get_max_price(self): pass
