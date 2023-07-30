from abc import ABC, abstractmethod


class BaseEnquiryHandler(ABC):

    @abstractmethod
    def handle(self, enquiry: str):
        raise NotImplementedError("subclass must implement handle method !!!")
