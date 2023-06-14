from .base_state import State


class CashDispensingState(State):

    def __init__(self, atm):
        self.atm = atm
