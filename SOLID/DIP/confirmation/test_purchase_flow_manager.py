from sms_notification_processor import SmsNotificationProcessor
from upi_payment_processor import UpiPaymentProcessor
from net_banking_payment_processor import NetBankingProcessor
from email_notification_processor import EmailNotificationProcessor
from purchase_flow_manager import PurchaseFlowManager

"""
- This principle is also called as 'Dependency Injection Principle' as client can inject which concreate class to use 
 in purchase manager
 
- This gives a greater flexibility to the client
"""


if __name__ == "__main__":
    US_purchase_flow_manager = PurchaseFlowManager(UpiPaymentProcessor(), SmsNotificationProcessor())
    US_purchase_flow_manager.trigger_purchase_flow(customer_id="CUST001", order_id="OD001")

    NE_purchase_flow_manager = PurchaseFlowManager(NetBankingProcessor(), EmailNotificationProcessor())
    NE_purchase_flow_manager.trigger_purchase_flow(customer_id="CUST002", order_id="OD002")