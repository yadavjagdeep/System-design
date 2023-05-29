
class PurchaseFlowManager:

    def __init__(self, payment_processor: object, notification_processor: object):
        self.PaymentProcessor = payment_processor
        self.NotificationProcessor = notification_processor

    def trigger_purchase_flow(self, order_id, customer_id):
        self.PaymentProcessor.process_payment(order_id, customer_id)
        self.NotificationProcessor.process_notification(order_id, customer_id)

"""
- Above class now depends only on abstract class of notification and payment class rather than concreate classes
"""