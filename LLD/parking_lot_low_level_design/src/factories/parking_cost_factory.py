from parking_lot_low_level_design.src.models.parking_cost.bike_parking_cost import BikeParkingCost
from parking_lot_low_level_design.src.models.parking_cost.truck_parking_cost import TruckParkingCost
from parking_lot_low_level_design.src.models.parking_cost.car_parking_cost import CarParkingCost
from parking_lot_low_level_design.src.models.vehicles.vehicle import VehicleTypes


class ParkingCostFactory:

    __MAP = {
        VehicleTypes.BIKE.value: BikeParkingCost,
        VehicleTypes.CAR.value: CarParkingCost,
        VehicleTypes.TRUCK.value: TruckParkingCost
    }

    @classmethod
    def get_parking_cost(cls, vehicle_type: str):
        parking_cost = cls.__MAP.get(vehicle_type)

        if not parking_cost:
            raise ValueError(f"Unknown vehicle type - {vehicle_type}")

        return parking_cost
