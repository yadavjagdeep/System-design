class DBAccessor:

    @staticmethod
    def get_atm_state(machine_id):
        return None

    @staticmethod
    def create_new_transaction(machine_id):
        return ""

    @staticmethod
    def update_atm_state(machine_id, new_state: str):
        return ""

    @staticmethod
    def get_card_details(card_number: str):
        # fetch card details from DB
        response = {
            "name_on_card": "ANKIT RAI",
            "card_number": "1234-5678-0879-9021",
            "expiry": "12/22",
            "cvv": 123
        }
        return response

    @staticmethod
    def get_transaction_data(transaction_id):
        return {}

    @staticmethod
    def update_transaction_details(transaction_id, data):
        return None
