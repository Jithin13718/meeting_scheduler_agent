from fastapi import APIRouter
from typing import List
from app.models.meeting import Meeting
from app.agents.optimizer import optimize_schedule

router = APIRouter()

@router.post("/")
def optimize(meetings: List[Meeting]):
    """
    Optimize a list of meetings to reduce conflicts.
    """
    optimized = optimize_schedule([m.dict() for m in meetings])
    return optimized