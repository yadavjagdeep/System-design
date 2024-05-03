from pydantic import BaseModel
from typing import Optional

data_map = {

}


class BaseException(Exception):
    status_code = 400
    message = "Exception occured"

    def __init__(self, message=None, status_code=None):
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        super(BaseException, self).__init__(self.message)


class RecordExistsException(BaseException):
    message = "Data exits with the passed short url"


class NoDataFound(BaseException):
    status_code = "400"
    message = "No record in db for passed key"


class TinyUrlModel(BaseModel):
    originalUrl: str
    shortUrl: str  # using short url as a primary key of table to make query faster
    expiry: int = 124232121


class URLStore:

    @staticmethod
    def insert(data: dict):
        validated_data = TinyUrlModel(**data)

        if validated_data.shortUrl in data_map:
            raise RecordExistsException(f"A record already exists with key = {validated_data.shortUrl}")
        data_map[validated_data.shortUrl] = data.__dict__

    @staticmethod
    def get(key: str):
        data = data_map.get(key, None)
        if not data:
            raise NoDataFound
        return data