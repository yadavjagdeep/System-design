from .base_state import State


class CardEjectingState(State):

    def __init__(self, atm: object):
        self.atm = atm
