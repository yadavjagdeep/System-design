from abc import ABC, abstractmethod

from queue import Queue
from models.elevator_controller import ElevatorController


class ElevatorControlStrategy(ABC):

    @abstractmethod
    def move_elevator(self, pending_requests: Queue, elevator_controller: ElevatorController):
        raise NotImplementedError
