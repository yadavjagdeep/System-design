from parking_lot_low_level_design.src.models.parking_cost.parking_cost import ParkingCost
from parking_lot_low_level_design.src.constants import VehicleTypes

class TruckParkingCost(ParkingCost):

    def __init__(self,
                 id: str,
                 garageId: str,
                 hourly: float,
                 daily: float,
                 monthly: float,
                 vehicleType: VehicleTypes = VehicleTypes.TRUCK.value):
        super().__init__(id, garageId, vehicleType, hourly, daily, monthly)