from abc import ABC


class State(ABC):

    def initialize(self):
        raise NotImplementedError

    def read_card(self, card_details: object):
        raise NotImplementedError

    def cancel_transaction(self, transaction_id: int):
        raise NotImplementedError

    def read_withdrawal_details(self, card_details: object, transaction_id: int, amount: int):
        raise NotImplementedError

    def dispense_cash(self, transaction_id: int):
        raise NotImplementedError

    def eject_card(self):
        raise NotImplementedError

