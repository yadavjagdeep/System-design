from .base_handler import BaseHandler


class AuthorizationHandler(BaseHandler):

    def __init__(self, next_handler):
        self.__next_handler = next_handler

    def handle(self, request):
        print("Processing Authorization Handler ... ")
        self.__next_handler.handle()
        return True
