from typing import Optional, List

from parking_lot_low_level_design.src.factories.parking_spot_factory import ParkingSpotFactory
from parking_lot_low_level_design.src.models.base_model import BaseModel
from parking_lot_low_level_design.src.models.parking_spot.parking_spot import ParkingSpot
from parking_lot_low_level_design.src.models.vehicles.vehicle import Vehicle, VehicleTypes


class Garage(BaseModel):

    def __init__(self, id: str, name: str, zipcode: str, spots: Optional[List[ParkingSpot]] = None):
        self.id = id # primaryKey
        self.name = name
        self.zipcode = zipcode
        self.spots = spots if spots else []

    def add_spot(self, spot: ParkingSpot) -> None:
        self.spots.append(spot)
        self.update()


    def get_spot(self, spot_id: str) -> Optional[ParkingSpot]:
        return next((spot for spot in self.spots if spot.id == spot_id), None)


    def remove_spot(self, spot_id: str) -> None:
        self.spots = [spot for spot in self.spots if spot.id != spot_id]
        self.update()


    def list_spots(self) -> list[ParkingSpot]:
        return self.spots


    @classmethod
    def get_spot_for_parking(cls, vehicle: Vehicle) -> Optional[ParkingSpot]:

        parking_spot_cls = ParkingSpotFactory.get_parking_spot(vehicle.vehicleType)

        for _, spot in parking_spot_cls.list_all().items():
            if not spot.isOccupied:
                return spot

        return None

