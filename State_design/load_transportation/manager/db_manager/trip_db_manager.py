class TripDBAccessor:

    @staticmethod
    def get_trip_data(trip_id):
        data = {
            "trip_id": "ID123",
            "origin": "Lucknow",
            "destination": "Delhi",
            "state": "in_transit"
        }
        return data

    @staticmethod
    def get_trip_state(trip_id: str):
        data = {
            "trip_id": "ID123",
            "origin": "Lucknow",
            "destination": "Delhi",
            "state": "in_transit"
        }
        return data.get("state", None)

    @staticmethod
    def update_trip_state(trip_id: str, state: str):
        return "update_success"

    @staticmethod
    def create_new_trip():
        return None

    @staticmethod
    def update_trip_data(trip_id, update_data):
        return True
