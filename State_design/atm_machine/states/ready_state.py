from .base_state import State
from State_design.atm_machine.db.db_accessor import DBAccessor
from State_design.atm_machine.ATM.atm_state import ATMState
from State_design.atm_machine.factories import StateFactory


class Ready_state(State):
    def __init__(self, atm: object):
        self.atm = atm

    def initialize(self):
        transaction_id: int = DBAccessor.create_new_transaction(self.atm.machine_id)
        if not transaction_id:
            raise RuntimeError("Unable to start transaction")
        self.atm.change_state(StateFactory.get_state(ATMState.CARD_READING.value, self.atm))
        return transaction_id

    def get_state_name(self):
        return ATMState.READY.value


