from State_design.load_transportation.manager.trip_state_manager.base_trip_state import BaseTripState
from State_design.load_transportation.manager.db_manager.trip_db_manager import TripDBAccessor
from State_design.load_transportation.constants import TripStates
from State_design.load_transportation.factories.trip_state_factory import TripStateFactory
from State_design.load_transportation.models.data_models import ArrivalData


class Requested(BaseTripState):

    def truck_arrived(self, trip_id: str, arrival_data: ArrivalData):
        trip_data = TripDBAccessor.get_trip_data(trip_id)
        if not trip_data:
            raise RuntimeError(f"Unable to get data for the provided trip_id !!!")
        TripDBAccessor.update_trip_data(trip_id, arrival_data)
        self.trip.change_state(TripStateFactory.get_trip_state(TripStates.MARK_IN.value, self.trip))

    def cancel_trip(self, trip_id: str, cancel_data: object):
        trip_data: dict = TripDBAccessor.get_trip_data(trip_id)
        if not trip_data:
            raise Exception(f"Trip id does not exists = {trip_id}")
        if not TripDBAccessor.update_trip_data(trip_id, cancel_data):
            raise Exception("failed to cancel trip !!!")
        self.trip.change_state(TripStateFactory.get_trip_state(state=TripStates.CANCELLED.value, trip=self.trip))

    def get_state_name(self):
        return TripStates.REQUESTED.value

