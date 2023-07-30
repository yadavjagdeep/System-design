from ..handler.validation_handler import ValidationHandler
from ..handler.authorization_handler import AuthorizationHandler
from ..handler.authantication_handler import AuthenticationHandler
from ..handler.ideal_handler import IdealHandler


class RequestHandlerFactory:

    @staticmethod
    def get_request_handler(api_name: str):
        if api_name.lower() == "play_video":
            return ValidationHandler(AuthenticationHandler(AuthorizationHandler(IdealHandler())))
        else:
            raise RuntimeError(f"Unknown Api name = {api_name}")
