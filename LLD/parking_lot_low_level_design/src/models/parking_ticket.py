from dataclasses import dataclass
from typing import Optional

from parking_lot_low_level_design.src.models.base_model import BaseModel
from parking_lot_low_level_design.src.models.parking_cost.parking_cost import ParkingCost


@dataclass
class ParkingTicket(BaseModel):
    id: str  # primaryKey
    garageId: str  # foreign key
    spotId: str  # foreign key
    entryTime: int
    exitTime: Optional[int] = None
    parkingCharge: Optional[float] = None


    def mark_out_vehicle(self, exit_time: int, parking_cost: ParkingCost):
        self.exitTime = exit_time
        self.parkingCharge = parking_cost.calculate_cost(self.entryTime, self.exitTime)
        self.update()
