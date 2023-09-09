from chaining_pattern.enquiry_handler.apis.enquiry_handler_api import EnquiryHandlerApi


def test_enquiry_api():
    EnquiryHandlerApi().process_request(request="")


if __name__ == "__main__":
    test_enquiry_api()
