from models.direction import Direction
from models.elevator_car import ElevatorCar
from models.floor import Floor


class ElevatorController:
    def __init__(self, elevator_car: ElevatorCar):
        self.elevator_car = elevator_car

    def accept_request(self, floor: Floor, direction: Direction):
        self.elevator_car.move(direction, floor)

    def control_elevator(self, floor: Floor, direction: Direction):
        self.elevator_car.move(direction, floor)


    def is_idle(self):
        return self.elevator_car.direction.value == Direction.IDLE.value
