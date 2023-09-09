from chaining_pattern.enquiry_handler.handler.base_enquiry_handler import BaseEnquiryHandler
from chaining_pattern.enquiry_handler.utilities.constants import EnquiryType


class IdleHandler(BaseEnquiryHandler):

    def handle(self, enquiry: str):
        print(f"Inside {self.__class__.__name__}")
        return EnquiryType.IDLE_ENQUIRY

