from State_design.load_transportation.manager.trip_state_manager.base_trip_state import BaseTripState
from State_design.load_transportation.manager.db_manager.trip_db_manager import TripDBAccessor
from State_design.load_transportation.factories.trip_state_factory import TripStateFactory
from State_design.load_transportation.models.data_models import LoadingData
from State_design.load_transportation.constants import TripStates


class MarkIn(BaseTripState):

    def load_truck(self, trip_id: str, loading_data: LoadingData):
        trip_data = TripDBAccessor.get_trip_data(trip_id)
        if not trip_data:
            raise RuntimeError(f"Trip with the provided id does not exists = {trip_id}")
        TripDBAccessor.update_trip_data(trip_id, loading_data)
        self.trip.change_state(TripStateFactory.get_trip_state(TripStates.LOADED.value, self.trip))

    def cancel_trip(self, trip_id: str, cancel_data: object):
        trip_data: dict = TripDBAccessor.get_trip_data(trip_id)
        if not trip_data:
            raise Exception(f"Trip id does not exists = {trip_id}")
        if not TripDBAccessor.update_trip_data(trip_id, cancel_data):
            raise Exception("failed to cancel trip !!!")
        self.trip.change_state(TripStateFactory.get_trip_state(state=TripStates.CANCELLED.value, trip=self.trip))

    def get_state_name(self):
        return TripStates.MARK_IN.value
