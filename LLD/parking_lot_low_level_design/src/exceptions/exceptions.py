class AppException(Exception):
    message = "Exception Occurred"
    status_code = 400

    def __init__(self, message=None, status_code=None):
        self.message = message if message else self.message
        self.status_code = status_code if status_code else self.status_code

    def __str__(self):
        return f'Status Code - {self.status_code}, Message - {self.message}'


class InvalidPayloadException(AppException):
    message = "InvalidPayload Exception"
