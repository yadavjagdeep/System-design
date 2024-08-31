from queue import Queue

from elevator_system_lld.strategies.elevator_control_strategy import ElevatorControlStrategy
from elevator_system_lld.strategies.elevator_control_strategy import ElevatorController


class ScanAlgorithm(ElevatorControlStrategy):
    def move_elevator(self, pending_requests: Queue, elevator_controller: ElevatorController):
        raise NotImplementedError
