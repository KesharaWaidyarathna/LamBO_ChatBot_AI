from abc import ABC, abstractmethod


class ContactDetailService:
    @abstractmethod
    def get_email(self): pass
