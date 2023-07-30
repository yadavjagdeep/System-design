from abc import ABC
from abc import ABC, abstractmethod

class State(ABC):

    def initialize(self):
        raise RuntimeError("Applied action not allowed in current state")

    def read_card(self, card_details: object):
        raise RuntimeError("Applied action not allowed in current state")

    def cancel_transaction(self, transaction_id: int):
        raise RuntimeError("Applied action not allowed in current state")

    def read_withdrawal_details(self, card_details: object, transaction_id: int, amount: int):
        raise RuntimeError("Applied action not allowed in current state")

    def dispense_cash(self, transaction_id: int):
        raise RuntimeError("Applied action not allowed in current state")

    def eject_card(self):
        raise RuntimeError("Applied action not allowed in current state")

    @abstractmethod
    def get_state_name(self):
        raise NotImplementedError("Subclass must implement the method !!!")


