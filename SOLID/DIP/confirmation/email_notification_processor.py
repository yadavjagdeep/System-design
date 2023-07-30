from notification_processor import NotificationProcessor

class EmailNotificationProcessor(NotificationProcessor):

    def process_notification(self, order_id, customer_id):
        print(f"Processing notification in = {self.__class__.__name__} for order_id = {order_id} and customer_id = {customer_id}")
        # Logic to process notification goes here
        return ""
