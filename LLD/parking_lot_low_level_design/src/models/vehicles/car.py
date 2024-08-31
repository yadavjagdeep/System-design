from parking_lot_low_level_design.src.models.vehicles.vehicle import Vehicle, VehicleTypes
from parking_lot_low_level_design.src.models.owner import Owner


class Car(Vehicle):

    def __init__(self,
                 id: str,
                 owner: Owner,
                 registrationNumber: str,
                 vehicleType = VehicleTypes.CAR.value
                 ):
        super().__init__(id, vehicleType, owner, registrationNumber)

