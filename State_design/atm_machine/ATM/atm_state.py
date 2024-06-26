from enum import Enum


class ATMState(Enum):
    READY = "READY"
    CARD_READING = "CARD_READING"
    WITHDRAWAL_DETAILS_READING = "WITHDRAWAL_DETAILS_READING"
    CASH_DISPENSING = "CASH_DISPENSING"
    CARD_EJECTING = "CARD_EJECTING"


