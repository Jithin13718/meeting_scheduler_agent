from pydantic import BaseModel
from typing import Optional, List

class Analytics(BaseModel):
    user_id: str
    total_meetings: int
    cancelled_meetings: int
    average_duration_minutes: float
    preferred_times: Optional[List[str]] = None