from parking_lot_low_level_design.src.models.base_model import BaseModel


class Owner(BaseModel):

    def __init__(self, id: str, name: str, phoneNumber: str, drivingLicense: str):
        self.id = id
        self.name = name
        self.phoneNumber = phoneNumber
        self.drivingLicense = drivingLicense

