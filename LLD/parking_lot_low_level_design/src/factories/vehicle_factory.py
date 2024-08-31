from parking_lot_low_level_design.src.models.parking_spot.truck_parking_spot import TruckParkingSpot
from parking_lot_low_level_design.src.models.vehicles.bike import Bike
from parking_lot_low_level_design.src.models.vehicles.car import Car
from parking_lot_low_level_design.src.models.vehicles.vehicle import VehicleTypes


class VehicleFactory:

    __MAP = {
        VehicleTypes.BIKE.value: Bike,
        VehicleTypes.CAR.value: Car,
        VehicleTypes.TRUCK.value: TruckParkingSpot
    }

    @classmethod
    def get_vehicle(cls, vehicle_type: str):
        vehicle = cls.__MAP.get(vehicle_type)

        if not vehicle:
            raise ValueError(f"Unknown vehicle type - {vehicle_type}")

        return vehicle
