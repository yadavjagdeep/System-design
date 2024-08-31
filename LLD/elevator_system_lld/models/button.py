from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def press_button(self, *args, **kwargs):
        raise NotImplementedError

class ExternalButton(Button):
    def __init__(self):
        self.dispatcher = None

    def press_button(self, floor, direction):
        if self.dispatcher is None:
            from elevator_system_lld.dispatcher.external_dispatcher import ExternalDispatcher
            self.dispatcher = ExternalDispatcher()
        from elevator_system_lld.models.floor import Floor
        from elevator_system_lld.models.direction import Direction
        self.dispatcher.submit_request(floor, direction)

class InternalButton(Button):
    def __init__(self):
        self.dispatcher = None

    def press_button(self, floor, direction, elevator_id):
        print(f'Button pressed for floor {floor.number} and direction {direction} in elevator {elevator_id}')
        if self.dispatcher is None:
            from elevator_system_lld.dispatcher.internal_dispatcher import InternalDispatcher
            self.dispatcher = InternalDispatcher()
        self.dispatcher.submit_request(floor, direction, elevator_id)