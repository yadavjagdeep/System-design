class AppException(Exception):
    message = "Exception Occurred"
    status_code = 400
    def __init__(self, message: str=None, status_code: int=None):
        self.message = message if message else self.message
        self.status_code = status_code if status_code else self.status_code

    def __str__(self):
        return f'Status Code - {self.status_code} and Message - {self.message}'



class InvalidDataException(AppException):
    message = "Invalid Data"


class NotFoundException(AppException):
    message = "Not Found"


class StorageFullException(AppException):
    message = "Storage Full"

