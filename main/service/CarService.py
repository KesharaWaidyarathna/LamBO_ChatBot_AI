from abc import ABC, abstractmethod


class CarService(ABC):
    @abstractmethod
    def get_car_details(self): pass

    @abstractmethod
    def get_car_color(self): pass

    @abstractmethod
    def get_car_by_brand(self, brand): pass

    @abstractmethod
    def get_price_ranges(self): pass
