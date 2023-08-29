from State_design.load_transportation.manager.trip_state_manager.base_trip_state import BaseTripState
from State_design.load_transportation.manager.db_manager.trip_db_manager import TripDBAccessor
from State_design.load_transportation.factories.trip_state_factory import TripStateFactory
from State_design.load_transportation.constants import TripStates


class Loaded(BaseTripState):

    def move_to_in_transit(self, trip_id: str):
        trip_data = TripDBAccessor.get_trip_data(trip_id)
        if not trip_data:
            raise RuntimeError(f"Trip with the provided id does not exists = {trip_id}")
        self.trip.change_state(TripStateFactory.get_trip_state(TripStates.IN_TRANSIT.value, self.trip))

    def get_state_name(self):
        return TripStates.LOADED.value
