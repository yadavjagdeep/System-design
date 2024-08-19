from parking_lot_low_level_design.src.models.parking_spot.car_parking_spot import CarParkingSpot
from parking_lot_low_level_design.src.models.parking_spot.bike_parking_spot import BikeParkingSpot
from parking_lot_low_level_design.src.models.parking_spot.truck_parking_spot import TruckParkingSpot
from parking_lot_low_level_design.src.models.vehicles.vehicle import VehicleTypes


class ParkingSpotFactory:

    __MAP = {
        VehicleTypes.BIKE.value: BikeParkingSpot,
        VehicleTypes.CAR.value: CarParkingSpot,
        VehicleTypes.TRUCK.value: TruckParkingSpot
    }

    @classmethod
    def get_parking_spot(cls, vehicle_type: str):
        spot = cls.__MAP.get(vehicle_type)

        if not spot:
            raise ValueError(f"Unknown vehicle type - {vehicle_type}")

        return spot
