from dataclasses import dataclass
from enum import Enum

from parking_lot_low_level_design.src.storage.in_memory_storage import InMemoryStorage
from parking_lot_low_level_design.src.models.base_model import BaseModel
from parking_lot_low_level_design.src.models.owner import Owner


class VehicleTypes(Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"


class Vehicle(BaseModel):

    def __init__(self, id: str, vehicleType: str, owner: Owner, registrationNumber: str):
        self.id = id
        self.vehicleType = vehicleType
        self.owner = owner
        self.registrationNumber = registrationNumber
