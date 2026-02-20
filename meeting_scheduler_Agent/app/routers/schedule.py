from fastapi import APIRouter
from app.models.meeting import Meeting
from app.agents.availability import check_availability

router = APIRouter()

@router.post("/create")
def create_meeting(meeting: Meeting):
    """
    Create a meeting and check availability.
    """
    availability = check_availability(calendar_data={"events": [meeting.dict()]})
    return {
        "message": "Meeting created",
        "meeting": meeting.dict(),
        "availability": availability
    }