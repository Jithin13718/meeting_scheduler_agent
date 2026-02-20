from fastapi import APIRouter, Depends
from app.dependencies import get_api_key, get_current_user

router = APIRouter()

@router.get("/secure-data")
def secure_endpoint(
    api_key: str = Depends(get_api_key),
    user: dict = Depends(get_current_user)
):
    return {"message": "Secure data accessed", "user": user}