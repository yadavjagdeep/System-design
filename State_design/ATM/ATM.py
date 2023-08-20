from atm_state import ATMState


class Atm:

    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.state = ATMState.READY

    def initialize_machine(self):
        if self.state.value == ATMState.CARD_READING.value:
            raise RuntimeError("Can't initialize currently in card reading states")
        if self.state.value == ATMState.CASH_DISPENSING.value:
            raise RuntimeError("Can't initialize currently in card reading states")

        # more such condition conditions in all the transition methods
        # This is because the next states of the atm depends on the current states


"""
To over this problem the 'states' that is changing can be made of polymorphic type 
"""

from State_design.factories.state_factory import StateFactory
from State_design.db.db_accessor import DBAccessor


class ATM:

    def __init__(self, machine_id: str):
        self.machine_id = machine_id
        self.state = StateFactory.get_state(DBAccessor.get_atm_state(self.machine_id), self)

    def initialize(self):
        return self.state.initialize()

    def read_card(self, card_details: object):
        return self.state.read_card(card_details)

    def cancel_transaction(self, transaction_id: int):
        return self.state.cancel_transaction(transaction_id)

    def read_withdrawal_details(self, card_details: object, transaction_id: int, amount: int):
        return self.state.read_withdrawal_details(card_details, transaction_id, amount)

    def dispense_cash(self, transaction_id: int):
        return self.state.dispense_cash(transaction_id)

    def eject_card(self):
        return self.state.eject_card()

    def change_state(self, new_state: object):
        self.state = new_state
        DBAccessor.update_atm_state(self.machine_id, new_state.get_state_name)


