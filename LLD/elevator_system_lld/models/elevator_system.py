from models.elevator_car import ElevatorCar
from models.elevator_controller import ElevatorController
from models.floor import Floor
from strategies.elevator_control_strategy import ElevatorControlStrategy
from strategies.elevator_selection_strategy import ElevatorSelectionStrategy


class ElevatorSystem:
    _INSTANCE = None

    def __new__(cls):
        if not cls._INSTANCE:
            cls._INSTANCE = super(ElevatorSystem, cls).__new__(cls)
        return cls._INSTANCE

    @classmethod
    def get_instance(cls):
        return cls._INSTANCE


    def __init__(self):
        self.elevator_controllers = []
        self.elevator_selection_strategy = None
        self.elevator_control_strategy = None
        self.floors = []

    def add_elevator(self, elevator_car: ElevatorCar):
        elevator_controller = ElevatorController(elevator_car)
        self.elevator_controllers.append(elevator_controller)

    def remove_elevator(self, elevator_controller: ElevatorController):
        self.elevator_controllers.remove(elevator_controller)

    def add_floor(self, floor: Floor):
        self.floors.append(floor)

    def set_elevator_selection_strategy(self, elevator_selection_strategy: ElevatorSelectionStrategy):
        self.elevator_selection_strategy = elevator_selection_strategy

    def set_elevator_control_strategy(self, elevator_control_strategy: ElevatorControlStrategy):
        self.elevator_control_strategy = elevator_control_strategy

    def request_elevator(self, floor: Floor, direction):
        elevator_controller = self.elevator_selection_strategy.select_elevator(self.elevator_controllers, floor, direction)
        elevator_controller.accept_request(floor, direction)
        return elevator_controller
