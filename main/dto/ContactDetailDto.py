class ContactDetailDto:
    __c_id: int
    __c_address: str
    __c_number: str
    __c_email: str

    def __init__(self) -> None:
        super().__init__()

    def get__c_id(self):
        return self.__c_id

    def get__c_address(self):
        return self.__c_address

    def get__c_number(self):
        return self.__c_number

    def get__c_email(self):
        return self.__c_email

    def set__c_id(self, __c_id):
        self.__c_id = __c_id

    def set__c_address(self, __c_address):
        self.__c_address = __c_address

    def set__c_number(self, __c_number):
        self.__c_number = __c_number

    def set__c_email(self, __c_email):
        self.__c_email = __c_email
