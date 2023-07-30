from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, order_id, customer_id):
        raise NotImplementedError("Implement in subclass")