from State_design.load_transportation.manager.trip_state_manager.base_trip_state import BaseTripState
from State_design.load_transportation.constants import TripStates


class TripCompleted(BaseTripState):
    def get_state_name(self):
        return TripStates.TRIP_COMPLETED.value


