# from elevator_system_lld.models.direction import Direction
# from elevator_system_lld.models.floor import Floor


class Display:
    def __init__(self,
                 floor = None,
                 direction = None
                 ):
        self.floor = floor
        self.direction = direction


    def set_floor(self, floor):
        self.floor = floor

    def set_direction(self, direction):
        self.direction = direction
