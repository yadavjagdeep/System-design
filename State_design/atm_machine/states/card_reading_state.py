from .base_state import State
from State_design.atm_machine.models import CardDetails
from State_design.atm_machine.db.db_accessor import DBAccessor
from State_design.atm_machine.factories import StateFactory
from State_design.atm_machine.ATM.atm_state import ATMState


class CardReadingState(State):

    def __init__(self, atm: object):
        self.atm = atm

    def read_card(self, card_details: CardDetails):
        card_details_from_db = DBAccessor.get_card_details(card_details.card_number)
        if not card_details_from_db:
            return self.atm.change_state(StateFactory.get_state(ATMState.CARD_EJECTING.value, self.atm))
        # Do validation on card data
        # …...
        # once all validation passed
        self.atm.change_state(StateFactory.get_state(ATMState.WITHDRAWAL_DETAILS_READING.value, self.atm))

    def cancel_transaction(self, transaction_id: int):
        transaction_data = DBAccessor.get_transaction_data(transaction_id)
        if not transaction_data:
            raise RuntimeError("Invalid transaction_id !!!")
        self.atm.change_state(StateFactory.get_state(ATMState.READY.value, self.atm))

    def get_state_name(self):
        return ATMState.CARD_READING.value
