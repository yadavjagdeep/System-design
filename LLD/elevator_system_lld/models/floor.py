from elevator_system_lld.models.button import Button
from elevator_system_lld.models.direction import Direction
from elevator_system_lld.models.display import Display


class Floor:

    def __init__(self,
                 number: int,
                 button: Button,
                 display: Display
                 ):
        self.number = number
        self.button = button
        self.display = display

    def press_button(self, direction: Direction):
        self.button.press_button(self, direction)


    # called every time an elevator elevator_car reaches every floor
    def set_display(self, floor, direction: Direction):
        self.display.direction = direction
        self.display.floor = floor
