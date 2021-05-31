class CarDto:
    __car_id: int
    __car_name: str
    __car_brand: str
    __color: str
    __speed: int
    __price: float

    def __init__(self) -> None:
        super().__init__()

    def get_car_id(self):
        return self.__car_id

    def get_car_name(self):
        return self.__car_name

    def get_car_brand(self):
        return self.__car_brand

    def get_color(self):
        return self.__color

    def get_speed(self):
        return self.__speed

    def get_price(self):
        return self.__price

    def set_car_id(self, car_id):
        self.__car_id = car_id

    def set_car_name(self, car_name):
        self.__car_name = car_name

    def set_car_brand(self, car_brand):
        self.__car_brand = car_brand

    def set_color(self, color):
        self.__color = color

    def set_speed(self, speed):
        self.__speed = speed

    def set_price(self, price):
        self.__price = price
