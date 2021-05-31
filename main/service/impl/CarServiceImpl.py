from main.dto.CarDto import CarDto
from main.repository.impl.CarRepositoryImpl import CarRepositoryImpl
from main.service.CarService import CarService


class CarServiceImpl(CarService):
    __carRepository: CarRepositoryImpl

    def __init__(self) -> None:
        self.__carRepository = CarRepositoryImpl()

    def get_car_details(self):
        carList = self.__carRepository.get_all()

        return self.__initialize_car_dto_list(carList)

    def get_car_color(self):
        carList = self.__carRepository.get_colors()
        return self.__initialize_car_dto_list(carList)

    def get_car_by_brand(self, brand):
        carList = self.__carRepository.find_by_brand(brand)
        return self.__initialize_car_dto_list(carList)

    def __initialize_car_dto_list(self, carList):
        carDtoList = []
        for car in carList:
            carDto = CarDto()
            carDto.set_car_id(car[0])
            carDto.set_car_name(car[1])
            carDto.set_car_brand(car[2])
            carDto.set_color(car[3])
            carDto.set_speed(car[4])
            carDto.set_price(car[5])
            carDtoList.append(carDto)

        return carDtoList

    def get_price_ranges(self):
        priceRange = []
        minPriceResult = self.__carRepository.get_min_price()
        maxPriceResult = self.__carRepository.get_max_price()
        priceRange.append(minPriceResult[0])
        priceRange.append(maxPriceResult[0])

        return priceRange
