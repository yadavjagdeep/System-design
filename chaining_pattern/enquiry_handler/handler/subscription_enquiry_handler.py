from enquiry_handler.handler.base_enquiry_handler import BaseEnquiryHandler
from enquiry_handler.utilities.constants import EnquiryType


class SubscriptionEnquiryHandler(BaseEnquiryHandler):

    def __init__(self, next_enquiry_handler: object):
        self.next_handler = next_enquiry_handler

    def handle(self, enquiry: str):
        print(f"Inside {self.__class__.__name__}")
        if 'month' or 'subscription' in enquiry:
            # Handle enquiry
            return EnquiryType.SUBSCRIPTION_ENQUIRY
        return self.next_handler.handle(enquiry)

