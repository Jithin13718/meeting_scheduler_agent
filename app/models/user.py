from pydantic import BaseModel
from typing import Optional, Dict, List

class User(BaseModel):
    id: str
    name: str
    email: str
    preferences: Optional[Dict[str, List[str]]] = None