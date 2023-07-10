from .base_state import State


class CardReadingState(State):

    def __init__(self, atm: object):
        self.atm = atm
