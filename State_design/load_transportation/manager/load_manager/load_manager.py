from State_design.load_transportation.factories.trip_state_factory import TripStateFactory
from State_design.load_transportation.manager.db_manager.trip_db_manager import TripDBAccessor
from State_design.load_transportation.models.data_models import (LoadingData, UnloadingData,
                                                                 PodData, CancelData, ArrivalData)


class Trip:

    def __init__(self, trip_id: str):
        self.trip_id = trip_id
        self.state = TripStateFactory.get_trip_state(TripDBAccessor.get_trip_state(self.trip_id), self)

    def initiate_trip(self):
        self.state.initiate_trip()

    def truck_arrived(self, trip_id: str, arrival_data: ArrivalData):
        self.state.truck_arrived(trip_id=trip_id, arrival_data=arrival_data)

    def load_truck(self, trip_id: str, loading_data: LoadingData):
        self.state.load_truck(trip_id=trip_id, loading_data=loading_data)

    def move_to_in_transit(self, trip_id: str):
        self.state.move_to_in_transit(trip_id=trip_id)

    def unload_truck(self, trip_id, unloading_data: UnloadingData):
        self.state.unload_truck(trip_id=trip_id, unloading_data=unloading_data)

    def pod_upload(self, trip_id, pod_data: PodData):
        self.state.pod_upload(trip_id=trip_id, pod_data=pod_data)

    def cancel_trip(self, trip_id: str, cancel_data: CancelData):
        self.state.cancel_trip(trip_id=trip_id, cancel_data=cancel_data)

    def change_state(self, new_state: object):
        self.state = new_state
        TripDBAccessor.update_trip_state(self.trip_id, new_state.get_state_name())
