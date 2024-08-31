from elevator_system_lld.models.elevator_car import ElevatorCar


class Door:

    def open(self, elevator_car: ElevatorCar):
        print(f"Door open of elevator - {elevator_car.number}")

    def close(self, elevator_car: ElevatorCar):
        print(f"Door closed of elevator - {elevator_car.number}")
