# from elevator_system_lld.models.button import Button
from elevator_system_lld.models.direction import Direction
# from elevator_system_lld.models.display import Display
# from elevator_system_lld.models.door import Door
# from elevator_system_lld.models.floor import Floor


class ElevatorCar:

    def __init__(self,
                 number: int,
                 door,
                 buttons,
                 display,
                 current_floor = -1,
                 direction = Direction.IDLE):
        self.number = number
        self.door = door
        self.button = buttons
        self.display = display
        self.current_floor = current_floor
        self.direction = direction

    def move(self, direction: Direction, floor):
        print(f'Elevator {self.number} moving {direction}')
        print(f'Elevator {self.number} reached floor {floor.number}')
        self.current_floor = floor.number
        self.door.open(self)
        self.door.close(self)
        self.set_display()

    def press_button(self, floor):
        direction = Direction.IDLE
        if floor.number > self.current_floor:
            direction = Direction.UP
        elif floor.number < self.current_floor:
            direction = Direction.DOWN

        self.button.press_button(floor, direction, self.number)


    def set_display(self):
        self.display.floor = self.current_floor
        self.display.direction = self.direction
