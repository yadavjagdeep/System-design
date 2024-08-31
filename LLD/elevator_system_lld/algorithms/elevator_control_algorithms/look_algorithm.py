from elevator_system_lld.models.elevator_controller import ElevatorController
from elevator_system_lld.strategies.elevator_control_strategy import ElevatorControlStrategy


class FirstComeFirstServe(ElevatorControlStrategy):
    def move_elevator(self, pending_requests: Queue, elevator_controller: ElevatorController):
        raise NotImplementedError
