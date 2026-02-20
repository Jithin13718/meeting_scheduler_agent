from fastapi import APIRouter
from app.models.user import User
from app.agents.preferences import learn_preferences

router = APIRouter()

@router.post("/create")
def create_user(user: User):
    """
    Create a new user with preferences.
    """
    return {"message": "User created", "user": user.dict()}

@router.post("/preferences")
def get_user_preferences(user: User):
    """
    Learn user preferences from history using ScaleDown.
    """
    preferences = learn_preferences(user.preferences or {})
    return {"user_id": user.id, "preferences": preferences}