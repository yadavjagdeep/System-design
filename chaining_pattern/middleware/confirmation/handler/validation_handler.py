from .base_handler import BaseHandler


class ValidationHandler(BaseHandler):

    def __init__(self, next_handler):
        self.__next_handler = next_handler

    def handle(self, request):
        print("process validation handler ... ")
        self.__next_handler.handle(request)
        return True

