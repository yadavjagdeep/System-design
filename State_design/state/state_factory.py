from State_design.ATM.atm_state import ATMState
from ready_state import Ready_state
from card_reading_state import CardReadingState
from cash_withdrwal_state import CashWithdrawalState
from cash_dispensing_state import CashDispensingState
from card_ejecting_state import CardEjectingState


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
            return CashWithdrawalState(ATM)
        else:
            return Ready_state(ATM)
