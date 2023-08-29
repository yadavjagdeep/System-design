from .base_state import State
from State_design.atm_machine.ATM.ATM import ATMState
from State_design.atm_machine.models import CardDetails
from State_design.atm_machine.db.db_accessor import DBAccessor
from State_design.atm_machine.factories import StateFactory


class CashWithdrawalDetailsReadingState(State):

    def __init__(self, atm: object):
        self.atm = atm

    def read_withdrawal_details(self, card_details: CardDetails, transaction_id: int, amount: int):
        card_data_from_db = DBAccessor.get_card_details(card_details.card_number)
        if not card_data_from_db:
            print("invalid card details !!! ")
            self.atm.change_state(StateFactory.get_state(ATMState.CARD_EJECTING.value, self.atm))
        # Do other stuff related to withdrawal details
        # if everything is good
        self.atm.change_state(StateFactory.get_state(ATMState.CASH_DISPENSING.value, self.atm))

    def cancel_transaction(self, transaction_id: int):
        transaction_details = DBAccessor.get_transaction_data(transaction_id)
        if not transaction_details:
            print("No data found for the transaction_id !!! ")
            self.atm.change_state(StateFactory.get_state(ATMState.CARD_EJECTING.value, self.atm))

    def get_state_name(self):
        return ATMState.WITHDRAWAL_DETAILS_READING.value
