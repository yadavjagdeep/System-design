class PlayVideoApi:

    def __init__(self, request_handlers: list):
        self.request_handlers: list = request_handlers

    def process_request(self, request: object):
        self.handle(request)
        pass

    def handle(self, request):
        for request_handler in self.request_handlers:
            request_handler.handle(request)


"""
There are few Problem with the above approach.
1. let's have a case where is second handler fails then we need to catch in H1 and take a call, we cannot do that here
2. If there a a request where H1 first needs to call H2 and so on and H1 gets executed on response of H1, 
we cannot support that
"""

"""
In our case the handler needs to know the next handler

"""
