from dataclasses import dataclass
import datetime

from parking_lot_low_level_design.src.storage.in_memory_storage import InMemoryStorage
from parking_lot_low_level_design.src.models.base_model import BaseModel
from parking_lot_low_level_design.src.constants import VehicleTypes

@dataclass
class ParkingCost(BaseModel):
    id: str # primaryKey
    garageId: str  # foreign key
    vehicleType: VehicleTypes
    hourly: float
    monthly: float
    daily: float


    def calculate_cost(self, entry_time: int, exit_time: int) -> float:
        # Convert epoch times to datetime objects
        entry_dt = datetime.datetime.fromtimestamp(entry_time)
        exit_dt = datetime.datetime.fromtimestamp(exit_time)

        # Calculate duration in days
        duration_days = (exit_dt - entry_dt).days
        duration_hours = (exit_dt - entry_dt).total_seconds() / 3600  # Total hours

        # Determine cost
        if duration_hours < 24:
            return self.hourly * duration_hours
        elif duration_days < 30:
            return self.daily * duration_days
        else:
            # For monthly rates, consider a simplified approach:
            # Round up to the nearest month
            months = (duration_days // 30) + 1
            return self.monthly * months

    def apply_discount(self, discount_percentage: float) -> None:
        """
        Apply a discount to all cost types.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        self.hourly -= self.hourly * (discount_percentage / 100)
        self.daily -= self.daily * (discount_percentage / 100)
        self.monthly -= self.monthly * (discount_percentage / 100)

