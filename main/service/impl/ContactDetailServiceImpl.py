from main.dto.ContactDetailDto import ContactDetailDto
from main.repository.impl.ContactDetailRepositoryImpl import ContactDetailRepositoryImpl
from main.service.ContactDetailService import ContactDetailService


class ContactDetailServiceImpl(ContactDetailService):
    __contactDetailRepository: ContactDetailRepositoryImpl
    __contactDetailDto: ContactDetailDto

    def __init__(self) -> None:
        self.__contactDetailRepository = ContactDetailRepositoryImpl()

    def get_email(self):
        contactDetailResult = self.__contactDetailRepository.get_email()
        return self.initialize_contact_detail_dto(contactDetailResult)

    def initialize_contact_detail_dto(self, contactDetailResult):
        self.__contactDetailDto = ContactDetailDto()
        self.__contactDetailDto.set__c_id(contactDetailResult[0])
        self.__contactDetailDto.set__c_address(contactDetailResult[1])
        self.__contactDetailDto.set__c_number(contactDetailResult[2])
        self.__contactDetailDto.set__c_email(contactDetailResult[3])

        return self.__contactDetailDto
