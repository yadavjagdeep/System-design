from abc import ABC, abstractmethod

class NotificationProcessor(ABC):

    @abstractmethod
    def process_notification(self, order_id, customer_id):
        raise NotImplementedError("Implement in subclass")
