from abc import ABC, abstractmethod
from State_design.load_transportation.models.data_models import (CancelData, LoadingData,
                                                                 UnloadingData, PodData, ArrivalData)


class BaseTripState(ABC):

    def __init__(self, trip: object):
        self.trip = trip

    # define all action that can be taken on different states
    def initiate_trip(self):
        raise RuntimeError("Applied action not allowed in current states")

    def truck_arrived(self, trip_id: str, arrival_data: ArrivalData):
        raise RuntimeError("Applied action not allowed in current states")

    def load_truck(self, trip_id: str, loading_data: LoadingData):
        raise RuntimeError("Applied action not allowed in current states")

    def move_to_in_transit(self, trip_id: str):
        raise RuntimeError("Applied action not allowed in current states")

    def unload_truck(self, trip_id, unloading_data: UnloadingData):
        raise RuntimeError("Applied action not allowed in current states")

    def pod_upload(self, trip_id, pod_data: PodData):
        raise RuntimeError("Applied action not allowed in current states")

    def cancel_trip(self, trip_id: str, cancel_data: CancelData):
        raise RuntimeError("Applied action not allowed in current states")

    @abstractmethod
    def get_state_name(self):
        raise NotImplementedError("Subclass must implement the method !!!")
