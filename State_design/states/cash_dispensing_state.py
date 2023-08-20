from State_design.states.base_state import State
from State_design.ATM.atm_state import ATMState
from State_design.db.db_accessor import DBAccessor
from State_design.factories.state_factory import StateFactory


class CashDispensingState(State):

    def __init__(self, atm):
        self.atm = atm

    def dispense_cash(self, transaction_id: int):
        transaction_details = DBAccessor.get_transaction_data(transaction_id)
        if not transaction_details:
            raise RuntimeError(f"No Transaction details found for, transaction_id = {transaction_id}")
        # Do validation
        # …...
        # once all validation passed
        updated_transaction_details = {}
        DBAccessor.update_transaction_details(transaction_id, updated_transaction_details)
        self.atm.change_state(StateFactory.get_state(ATMState.CARD_EJECTING.value, self.atm))

    def cancel_transaction(self, transaction_id: int):
        transaction_data = DBAccessor.get_transaction_data(transaction_id)
        if not transaction_data:
            raise RuntimeError("Invalid transaction_id !!!")
        self.atm.change_state(StateFactory.get_state(ATMState.CARD_EJECTING.value, self.atm))

    def get_state_name(self):
        return ATMState.CASH_DISPENSING.value
