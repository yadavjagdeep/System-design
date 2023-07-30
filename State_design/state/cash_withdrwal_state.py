from .base_state import State


class CashWithdrawalState(State):

    def __init__(self, atm: object):
        self.atm = atm
