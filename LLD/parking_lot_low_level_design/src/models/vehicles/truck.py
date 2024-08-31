from parking_lot_low_level_design.src.models.owner import Owner
from parking_lot_low_level_design.src.models.vehicles.vehicle import Vehicle, VehicleTypes


class Truck(Vehicle):

    def __init__(self,
                 id: str,
                 owner: Owner,
                 registrationNumber: str,
                 vehicleType=VehicleTypes.TRUCK.value
                 ):
        super().__init__(id, vehicleType, owner, registrationNumber)

