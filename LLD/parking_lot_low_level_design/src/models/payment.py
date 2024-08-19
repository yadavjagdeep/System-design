from dataclasses import dataclass

from parking_lot_low_level_design.src.constants import PaymentMode
from parking_lot_low_level_design.src.models.base_model import BaseModel


@dataclass
class Payment(BaseModel):   #  TODO: complete payment integration
    id: str  # primaryKey
    ticketId: str  # foreign Key
    paymentMode: PaymentMode
    paymentTime: int
