from queue import Queue

from elevator_system_lld.models.elevator_controller import ElevatorController
from elevator_system_lld.strategies.elevator_control_strategy import ElevatorControlStrategy


class FirstComeFirstServe(ElevatorControlStrategy):

    def move_elevator(self, pending_requests: Queue, elevator_controller: ElevatorController):
        if not pending_requests.empty():
            floor, direction = pending_requests.get()
            elevator_controller.control_elevator(floor, direction)

        raise Exception("No pending requests")
