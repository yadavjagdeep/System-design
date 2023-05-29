"""
 - Idea is a High-level module should not depend on low-level module, rather both should depend on abstraction
"""
" => will get more understanding with an example"

class PurchaseFlowManager:
    """
     - Two-step process
     1. complete payment
     2. send notification of payment success
    """

    def process_payment(self, order_id, customer_id):
        print("processing payment")
        # Logic to process payment goes here
        return ""

    def send_notification(self, order_id, customer_id):
        print("sending notification")
        # Logic to send notification goes here
        return ""

"""
- The above class has 2 main issues
1. It violates a basic design principe (SRP) Single responsibility principle, PurchaseFlowManager has to process payment ans send_notification
2. The PurchaseFlowManager is an external module so it should 'not depend on concreate implementation' of low-level modules like send_notification or
    process_payment, rather it should 'depend on abstraction'
"""
