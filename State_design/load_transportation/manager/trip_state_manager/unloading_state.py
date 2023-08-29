from State_design.load_transportation.manager.trip_state_manager.base_trip_state import BaseTripState
from State_design.load_transportation.factories.trip_state_factory import TripStateFactory
from State_design.load_transportation.constants import TripStates
from State_design.load_transportation.models.data_models import PodData
from State_design.load_transportation.manager.db_manager.trip_db_manager import TripDBAccessor


class Unloading(BaseTripState):

    def pod_upload(self, trip_id, pod_data: PodData):
        trip_data = TripDBAccessor.get_trip_data(trip_id)
        if not trip_data:
            raise RuntimeError(f"Trip with the provided id does not exists = {trip_id}")
        TripDBAccessor.update_trip_data(trip_id, pod_data)
        self.trip.change_state(TripStateFactory.get_trip_state(TripStates.TRIP_COMPLETED.value, self.trip))

    def get_state_name(self):
        return TripStates.UNLOADING.value


