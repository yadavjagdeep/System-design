from State_design.atm_machine.states.base_state import State
from State_design.atm_machine.ATM.atm_state import ATMState
from State_design.atm_machine.factories import StateFactory


class CardEjectingState(State):

    def __init__(self, atm: object):
        self.atm = atm

    def eject_card(self):
        print("Thank you for the transaction")
        self.atm.change_state(StateFactory.get_state(ATMState.READY.value, self.atm))

    def get_state_name(self):
        return ATMState.CARD_EJECTING.value
