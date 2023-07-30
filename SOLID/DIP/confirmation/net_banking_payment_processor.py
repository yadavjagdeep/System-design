from payment_processor import PaymentProcessor

class NetBankingProcessor(PaymentProcessor):

    def process_payment(self, order_id, customer_id):
        print(f"Processing payment in = {self.__class__.__name__} for order_id = {order_id} and customer_id = {customer_id}")
        # Logic to process payment goes here
        return ""