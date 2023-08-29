from pydantic import BaseModel
from typing import Optional


class LoadingData(BaseModel):
    lr_number: str
    ewb_numer: Optional[str]
    vehicle_number: str
    driver_number: Optional[str]
    driver_name: str
    loading_remark: Optional[str]


class UnloadingData(BaseModel):
    lr_number: str
    unloading_remark: Optional[str]


class CancelData(BaseModel):
    cancellation_reason: str
    cancellation_remark: str


class PodData(BaseModel):
    pod_type: str
    pod_file_url: Optional[str]


class ArrivalData(BaseModel):
    truck_number: str
