from main.db.DbConnection import DbConnection
from main.repository.ContactDetailRepository import ContactDetailRepository


class ContactDetailRepositoryImpl(ContactDetailRepository):
    __dbConn: DbConnection

    def __init__(self) -> None:
        self.__dbConn = DbConnection()

    def get_email(self):
        cursor = self.__dbConn.get_connection().cursor()
        cursor.execute("SELECT * FROM contact_details")
        return cursor.fetchone()
