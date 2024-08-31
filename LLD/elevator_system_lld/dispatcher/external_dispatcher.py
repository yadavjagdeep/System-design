from elevator_system_lld.models.direction import Direction
from elevator_system_lld.models.floor import Floor
from models.elevator_system import ElevatorSystem


class ExternalDispatcher:
    _INSTANCE = None

    def __new__(cls):
        if not cls._INSTANCE:
            cls._INSTANCE = super(ExternalDispatcher, cls).__new__(cls)
            cls._INSTANCE.__initialized = False
        return cls._INSTANCE

    @classmethod
    def get_instance(cls):
        return cls._INSTANCE


    def submit_request(self, floor: Floor, direction: Direction) -> None:
        _elevator_system = ElevatorSystem.get_instance()
        elevator = _elevator_system.elevator_selection_strategy.select_elevator(
            _elevator_system.elevator_controllers, floor, direction)

        print(f"Request submitted to elevator {elevator.elevator_id}")
        elevator.accept_request(floor, direction)



