from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Meeting(BaseModel):
    id: Optional[str]
    title: str
    start_time: datetime
    end_time: datetime
    participants: List[str]
    location: Optional[str] = None
    description: Optional[str] = None