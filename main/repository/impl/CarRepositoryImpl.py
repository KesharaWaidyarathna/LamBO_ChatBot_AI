from main.db.DbConnection import DbConnection
from main.repository.CarRepository import CarRepository


class CarRepositoryImpl(CarRepository):
    __dbConn: DbConnection

    def __init__(self) -> None:
        self.__dbConn = DbConnection()

    def get_all(self):
        cursor = self.__dbConn.get_connection().cursor()

        cursor.execute("SELECT * FROM cars")
        return cursor.fetchall()

    def get_colors(self):
        cursor = self.__dbConn.get_connection().cursor()

        cursor.execute("SELECT * FROM cars")
        return cursor.fetchall()

    def find_by_brand(self, brand):
        cursor = self.__dbConn.get_connection().cursor()

        query = "SELECT * FROM cars WHERE cars.car_brand = %s"
        param = (brand,)
        cursor.execute(query, param)

        return cursor.fetchall()

    def get_min_price(self):
        cursor = self.__dbConn.get_connection().cursor()

        query = "SELECT MIN(price) FROM cars"
        cursor.execute(query)

        return cursor.fetchone()

    def get_max_price(self):
        cursor = self.__dbConn.get_connection().cursor()

        query = "SELECT MAX(price) FROM cars"
        cursor.execute(query)

        return cursor.fetchone()

