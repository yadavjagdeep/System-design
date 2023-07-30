from .base_handler import BaseHandler


class IdealHandler(BaseHandler):

    def handle(self, request):
        print("All Done ... ")
        return True


"""
We need this ideal handler to avoid null check at each handler, at any handler we may end up as no next handler
"""