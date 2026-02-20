from fastapi import APIRouter
from app.models.analytics import Analytics

router = APIRouter()

@router.post("/")
def get_analytics(analytics: Analytics):
    """
    Return analytics data for a user.
    """
    return {
        "user_id": analytics.user_id,
        "total_meetings": analytics.total_meetings,
        "cancelled_meetings": analytics.cancelled_meetings,
        "average_duration_minutes": analytics.average_duration_minutes,
        "preferred_times": analytics.preferred_times
    }