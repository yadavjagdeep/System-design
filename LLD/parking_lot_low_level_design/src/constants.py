from enum import Enum


class VehicleTypes(Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"


class PaymentMode(Enum):
    CASH = "cash"
    CARD = "card"
