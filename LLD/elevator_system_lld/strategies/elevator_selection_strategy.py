from abc import ABC, abstractmethod

from models.direction import Direction
from models.elevator_controller import ElevatorController
from models.floor import Floor


class ElevatorSelectionStrategy(ABC):

    @abstractmethod
    def select_elevator(self, elevator_controllers: list[ElevatorController], floor: Floor, direction: Direction):
        raise NotImplementedError
