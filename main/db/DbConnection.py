import mysql.connector


class DbConnection:
    __myDb = ()

    def __init__(self) -> None:
        self.__myDb = mysql.connector.connect(host="localhost", user="admin", passwd="root", database="lambo_car_sale")

    def get_connection(self):
        return self.__myDb
