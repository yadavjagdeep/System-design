from elevator_system_lld.models.direction import Direction
from elevator_system_lld.models.elevator_controller import ElevatorController
from elevator_system_lld.models.floor import Floor
from elevator_system_lld.strategies.elevator_selection_strategy import ElevatorSelectionStrategy


class Zone(ElevatorSelectionStrategy):
    def select_elevator(self, elevator_controllers: list[ElevatorController], floor: Floor, direction: Direction):
        raise NotImplementedError

