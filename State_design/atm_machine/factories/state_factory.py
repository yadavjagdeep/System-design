from State_design.atm_machine.ATM.atm_state import ATMState
from State_design.atm_machine.states.ready_state import Ready_state
from State_design.atm_machine.states.card_reading_state import CardReadingState
from State_design.atm_machine.states.cash_withdrawal_details_reading_state import CashWithdrawalDetailsReadingState
from State_design.atm_machine.states.cash_dispensing_state import CashDispensingState
from State_design.atm_machine.states.card_ejecting_state import CardEjectingState


class StateFactory:

    @staticmethod
    def get_state(state: str, ATM: object):
        if state == ATMState.CASH_DISPENSING.value:
            return CashDispensingState(ATM)
        elif state == ATMState.CARD_READING.value:
            return CardReadingState(ATM)
        elif state == ATMState.CARD_EJECTING.value:
            return CardEjectingState(ATM)
        elif state == ATMState.WITHDRAWAL_DETAILS_READING.value:
            return CashWithdrawalDetailsReadingState(ATM)
        else:
            return Ready_state(ATM)
