from .base_state import State
from State_design.db.db_accessor import DBAccessor
from State_design.ATM.atm_state import ATMState
from State_design.state.state_factory import StateFactory


class CardReadingState(State):

    def __init__(self, atm: object):
        self.atm = atm


    @classmethod
    def get_state_name(cls):
        return ATMState.CARD_READING.value
