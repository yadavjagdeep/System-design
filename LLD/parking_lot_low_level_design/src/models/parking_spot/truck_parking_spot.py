from parking_lot_low_level_design.src.models.parking_spot.parking_spot import ParkingSpot
from parking_lot_low_level_design.src.models.vehicles.vehicle import Vehicle, VehicleTypes


class TruckParkingSpot(ParkingSpot):
    def __init__(self,
                 id: str,
                 garageId: str,
                 spotNumber: int,
                 level: int,
                 isOccupied: bool = False,
                 vehicle: Vehicle = None,
                 vehicleType: VehicleTypes = VehicleTypes.TRUCK
                 ):
        super().__init__(id, garageId, spotNumber, level, vehicleType, isOccupied, vehicle)
