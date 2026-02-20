from fastapi import APIRouter

router = APIRouter()

@router.get("/callback")
def auth_callback(code: str):
    """
    Handle OAuth2 callback from Google.
    """
    # Placeholder: In real implementation, exchange 'code' for tokens
    return {"message": "OAuth callback received", "code": code}