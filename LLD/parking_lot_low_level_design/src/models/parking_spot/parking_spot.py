from parking_lot_low_level_design.src.models.vehicles.vehicle import Vehicle, VehicleTypes
from parking_lot_low_level_design.src.models.base_model import BaseModel


class ParkingSpot(BaseModel):


    def __init__(self,
                 id: str,
                 garageId: str,
                 spotNumber: int,
                 level: int,
                 vehicleType: VehicleTypes,
                 isOccupied: bool = False,
                 vehicle: Vehicle = None):
        self.id = id  # primaryKey
        self.garageId = garageId  # foreign key
        self.spotNumber = spotNumber
        self.level = level
        self.vehicleType = vehicleType
        self.isOccupied = isOccupied
        self.vehicle = vehicle


    def park_vehicle(self, vehicle: Vehicle) -> None:
        if self.isOccupied:
            raise Exception("Parking spot is not empty !!!")

        self.isOccupied = True
        self.vehicle = vehicle
        # Update the storage with the new state of the ParkingSpot
        self.update()


    def unpark_vehicle(self) -> Vehicle:
        if not self.isOccupied:
            raise Exception("Parking spot is already vacant.")

        self.isOccupied = False
        vehicle = self.vehicle
        self.vehicle = None

        # Update the storage with the new state of the ParkingSpot
        self.update()
        return vehicle


    def is_available(self) -> bool:
        return not self.isOccupied
