from elevator_system_lld.models.direction import Direction
from elevator_system_lld.models.floor import Floor
from models.elevator_system import ElevatorSystem


class InternalDispatcher:
    _INSTANCE = None

    def __new__(cls):
        if not cls._INSTANCE:
            cls._INSTANCE = super(InternalDispatcher, cls).__new__(cls)
        return cls._INSTANCE

    def submit_request(self, floor: Floor, direction: Direction, elevator_id: str) -> None:
        _elevator_system = ElevatorSystem.get_instance()
        for elevator_controller in _elevator_system.elevator_controllers:
            if elevator_controller.elevator_car.number == elevator_id:
                elevator_controller.accept_request(floor, direction)
                return

        raise Exception(f"Elevator with id {elevator_id} not found")
