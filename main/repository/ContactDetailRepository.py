from abc import ABC, abstractmethod


class ContactDetailRepository(ABC):

    @abstractmethod
    def get_email(self): pass
