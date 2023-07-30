from enquiry_handler.handler.base_enquiry_handler import BaseEnquiryHandler
from enquiry_handler.utilities.constants import EnquiryType


class IdleHandler(BaseEnquiryHandler):

    def handle(self, enquiry: str):
        print(f"Inside {self.__class__.__name__}")
        return EnquiryType.IDLE_ENQUIRY

