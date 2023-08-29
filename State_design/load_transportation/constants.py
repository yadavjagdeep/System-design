from enum import Enum


class TripStates(Enum):
    INITIATION = "initiation"
    REQUESTED = "requested"
    MARK_IN = "mark_in"
    LOADED = "loaded"
    IN_TRANSIT = "in_transit"
    UNLOADING = "unloading"
    TRIP_COMPLETED = "trip_completed"
    CANCELLED = "cancelled"
