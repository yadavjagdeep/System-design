from chaining_pattern.enquiry_handler.handler.base_enquiry_handler import BaseEnquiryHandler
from chaining_pattern.enquiry_handler.utilities.constants import EnquiryType


class AcademicEnquiryHandler(BaseEnquiryHandler):

    def __init__(self, next_enquiry_handler: object):
        self.next_handler = next_enquiry_handler

    def handle(self, enquiry: str):
        print(f"Inside {self.__class__.__name__}")
        if 'ds algo' or 'design' in enquiry:
            # Handle enquiry
            return EnquiryType.ACADEMIC_ENQUIRY
        return self.next_handler.handle(enquiry)
