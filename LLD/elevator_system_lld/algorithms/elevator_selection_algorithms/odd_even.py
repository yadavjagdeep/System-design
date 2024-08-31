from elevator_system_lld.models.direction import Direction
from elevator_system_lld.models.elevator_controller import ElevatorController
from elevator_system_lld.models.floor import Floor
from elevator_system_lld.strategies.elevator_selection_strategy import ElevatorSelectionStrategy


class OddEven(ElevatorSelectionStrategy):
    def select_elevator(self, elevator_controllers: list[ElevatorController], floor: Floor, direction: Direction):
        odd_even_elevators = [elevator for elevator in elevator_controllers if
                              elevator.elevator_car.number % 2 == floor.number % 2]

        for elevator in odd_even_elevators:
            if elevator.is_idle() or elevator.elevator_car.direction.value == direction.value:
                return elevator


        raise Exception("No suitable elevators available")
