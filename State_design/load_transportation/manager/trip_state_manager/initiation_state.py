from State_design.load_transportation.manager.trip_state_manager.base_trip_state import BaseTripState
from State_design.load_transportation.manager.db_manager.trip_db_manager import TripDBAccessor
from State_design.load_transportation.constants import TripStates
from State_design.load_transportation.factories.trip_state_factory import TripStateFactory


class InitiationState(BaseTripState):

    def initiate_trip(self):
        trip_id: str = TripDBAccessor.create_new_trip()
        if not trip_id:
            raise RuntimeError("Unable to create new transaction")
        self.trip.trip_id = trip_id
        self.trip.change_state(TripStateFactory.get_trip_state(state=TripStates.REQUESTED.value, trip=self.trip))
        return trip_id

    def get_state_name(self):
        return TripStates.INITIATION.value
