import time

from parking_lot_low_level_design.src.factories.parking_cost_factory import ParkingCostFactory
from parking_lot_low_level_design.src.factories.parking_spot_factory import ParkingSpotFactory
from parking_lot_low_level_design.src.factories.vehicle_factory import VehicleFactory
from parking_lot_low_level_design.src.models.garage import Garage
from parking_lot_low_level_design.src.models.vehicles.vehicle import VehicleTypes
from parking_lot_low_level_design.src.models.owner import Owner
from parking_lot_low_level_design.src.models.parking_ticket import ParkingTicket



if __name__ == "__main__":
    # Create garages
    garage1 = Garage(id="garage::1", name="khan garage", zipcode='201301').add()
    print(f'Garage created: {garage1.name} with ID {garage1.id}')

    garage2 = Garage(id="garage::2", name="pandit garage", zipcode='201305').add()
    print(f'Garage created: {garage2.name} with ID {garage2.id}')

    # Update a garage
    g1 = Garage.get("garage::1")
    g1.name = "yadav garage"
    g1.update()
    print(f'Garage updated: {g1.name} with ID {g1.id}')

    # Add parking costs for the garage
    ParkingCostFactory.get_parking_cost(VehicleTypes.CAR.value)(id=f"car-{g1.id}", garageId=g1.id, hourly=20, daily=200, monthly=1000).add()
    print('Car parking cost added for the garage')

    ParkingCostFactory.get_parking_cost(VehicleTypes.BIKE.value)(id=f"bike-{g1.id}", garageId=g1.id, hourly=10, daily=100, monthly=500).add()
    print('Bike parking cost added for the garage')

    ParkingCostFactory.get_parking_cost(VehicleTypes.TRUCK.value)(id=f"truck-{g1.id}", garageId=g1.id, hourly=30, daily=300, monthly=1500).add()
    print('Truck parking cost added for the garage')

    # Add parking spots
    car_spot = ParkingSpotFactory.get_parking_spot(VehicleTypes.CAR.value)(id="car-spot::1", garageId=g1.id, spotNumber=1, level=1).add()
    print(f'Car parking spot added: Spot Number {car_spot.spotNumber} at Level {car_spot.level}')

    bike_spot = ParkingSpotFactory.get_parking_spot(VehicleTypes.BIKE.value)(id="bike-spot::1", garageId=g1.id, spotNumber=2, level=1).add()
    print(f'Bike parking spot added: Spot Number {bike_spot.spotNumber} at Level {bike_spot.level}')

    truck_spot = ParkingSpotFactory.get_parking_spot(VehicleTypes.TRUCK.value)(id="truck-spot::1", garageId=g1.id, spotNumber=3, level=1).add()
    print(f'Truck parking spot added: Spot Number {truck_spot.spotNumber} at Level {truck_spot.level}')

    # Add owners and vehicles
    car1_owner = Owner(id="owner::1", name="Amit Kumar", phoneNumber="992144311", drivingLicense="DLI001").add()
    print(f'Owner added: {car1_owner.name} with ID {car1_owner.id}')

    car1 = VehicleFactory.get_vehicle(VehicleTypes.CAR.value)(id="car::1", owner=car1_owner, registrationNumber="RC-CAR-001").add()
    print(f'Car added: Registration Number {car1.registrationNumber} for Owner {car1.owner.name}')

    # Park the car
    parking_spot = Garage.get_spot_for_parking(car1)
    parking_spot.park_vehicle(car1)
    print(f'Car parked: {car1.registrationNumber} at Spot Number {parking_spot.spotNumber}')

    ticket1 = ParkingTicket(id="ticket-001", garageId=parking_spot.garageId, spotId=parking_spot.id, entryTime=int(time.time())-300).add()
    print(f'Parking ticket issued: Ticket ID {ticket1.id} for Car {car1.registrationNumber}')

    # Calculate and print parking charge
    parking_cost = ParkingCostFactory.get_parking_cost(parking_spot.vehicleType.value).get(f'{parking_spot.vehicleType.value}-{ticket1.garageId}')
    ticket1.mark_out_vehicle(exit_time=int(time.time()), parking_cost=parking_cost)
    print(f'Parking Charge: {ticket1.parkingCharge}')

    # Unpark the vehicle
    vehicle = parking_spot.unpark_vehicle()
    print(f'vehicle unparked: {vehicle.registrationNumber} from Spot Number {parking_spot.spotNumber}')

    # Park another vehicle and repeat the process
    car2_owner = Owner(id="owner::2", name="Sumit Kumar", phoneNumber="992144319", drivingLicense="DLI002").add()
    print(f'Owner added: {car2_owner.name} with ID {car2_owner.id}')

    car2 = VehicleFactory.get_vehicle(VehicleTypes.CAR.value)(id="car::2", owner=car2_owner, registrationNumber="RC-CAR-002").add()
    print(f'Car added: Registration Number {car2.registrationNumber} for Owner {car2.owner.name}')

    parking_spot = Garage.get_spot_for_parking(car2)
    parking_spot.park_vehicle(car2)
    print(f'Car parked: {car2.registrationNumber} at Spot Number {parking_spot.spotNumber}')