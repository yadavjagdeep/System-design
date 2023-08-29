from pydantic import BaseModel, ValidationError
from dataclasses import dataclass


# @dataclass
# class CardDetails:
#     name_on_card: str
#     card_number: str
#     expiry: str
#     cvv: int


class CardDetails(BaseModel):
    name_on_card: str
    card_number: str
    expiry: str
    cvv: int


# if __name__ == "__main__":
#     data = {
#         "name_on_card": "ANKIT RAI",
#         "card_number": "1234-5678-0879-9021",
#         "expiry": "12/22",
#         "cvv": 123
#     }
#     # resp = CardDetails(**data)
#     # print(resp)
#     try:
#         resp = CardDetails(**data)
#         print(resp)
#     except ValidationError as e:
#         print(e.errors())
#         print(repr(e.errors()[0]['type']))
