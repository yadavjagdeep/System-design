from enquiry_handler.factories.enquiry_handler_factory import RequestHandlerFactory


class EnquiryHandlerApi:

    def process_request(self, request):
        response = RequestHandlerFactory.get_enquiry_handler().handle(enquiry="Hi i want to upgrade my subscription")
        print(f"Enquiry type = {response}")
