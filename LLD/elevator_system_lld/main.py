from algorithms.elevator_control_algorithms.first_come_first_serve import FirstComeFirstServe
from algorithms.elevator_selection_algorithms.odd_even import OddEven
from models.button import Button, InternalButton, ExternalButton
from models.direction import Direction
from models.display import Display
from models.door import Door
from models.elevator_car import ElevatorCar
from models.elevator_system import ElevatorSystem
from models.floor import Floor


class ElevatorSystemApplication:

    _elevator_system = ElevatorSystem()
    _elevator_system.set_elevator_selection_strategy(OddEven())
    _elevator_system.set_elevator_control_strategy(FirstComeFirstServe())

    # 20 floors + 1 basement
    total_floors = 21
    for i in range(total_floors):
        _elevator_system.add_floor(Floor(number=i, button=ExternalButton(), display=Display()))

    # 5 elevators
    for i in range(1, 6):
        _elevator_system.add_elevator(ElevatorCar(number=i, door=Door(), buttons=InternalButton(), display=Display()))
        
    # Request an elevator at floor 1 to go to floor 10
    _elevator_controller1 = _elevator_system.request_elevator(_elevator_system.floors[10], Direction.UP)
    _elevator_controller1.elevator_car.press_button(_elevator_system.floors[20])

    # Request an elevator at floor 5 to go to floor 2
    _elevator_controller2 = _elevator_system.request_elevator(_elevator_system.floors[7], Direction.DOWN)
    _elevator_controller2.elevator_car.press_button(_elevator_system.floors[2])


if __name__ == '__main__':
    ElevatorSystemApplication()
