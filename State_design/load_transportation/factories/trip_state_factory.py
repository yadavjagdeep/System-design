from State_design.load_transportation.manager.trip_state_manager.cancelled_state import Cancelled
from State_design.load_transportation.manager.trip_state_manager.requested_state import Requested
from State_design.load_transportation.manager.trip_state_manager.mark_in_state import MarkIn
from State_design.load_transportation.manager.trip_state_manager.loaded_state import Loaded
from State_design.load_transportation.manager.trip_state_manager.in_transit import InTransit
from State_design.load_transportation.manager.trip_state_manager.trip_completed_state import TripCompleted
from State_design.load_transportation.manager.trip_state_manager.unloading_state import Unloading
from State_design.load_transportation.manager.trip_state_manager.initiation_state import InitiationState
from State_design.load_transportation.constants import TripStates


class TripStateFactory:

    @staticmethod
    def get_trip_state(state: str, trip: object):
        if state.lower() == TripStates.MARK_IN.value:
            return MarkIn(trip=trip)
        elif state.lower() == TripStates.LOADED.value:
            return Loaded(trip=trip)
        elif state.lower() == TripStates.IN_TRANSIT.value:
            return InTransit(trip=trip)
        elif state.lower() == TripStates.UNLOADING.value:
            return Unloading(trip=trip)
        elif state.lower() == TripStates.TRIP_COMPLETED.value:
            return TripCompleted(trip=trip)
        elif state.lower() == TripStates.CANCELLED.value:
            return Cancelled(trip=trip)
        elif state.lower() == TripStates.REQUESTED.value:
            return Requested(trip=trip)
        else:
            return InitiationState(trip=trip)
