from chaining_pattern.enquiry_handler.handler.academic_enquiry_handler import AcademicEnquiryHandler
from chaining_pattern.enquiry_handler.handler.project_enquiry_handler import ProjectEnquiryHandler
from chaining_pattern.enquiry_handler.handler.subscription_enquiry_handler import SubscriptionEnquiryHandler
from chaining_pattern.enquiry_handler.handler.idle_handler import IdleHandler


class RequestHandlerFactory:

    @staticmethod
    def get_enquiry_handler():
        return AcademicEnquiryHandler(ProjectEnquiryHandler(SubscriptionEnquiryHandler(IdleHandler)))

