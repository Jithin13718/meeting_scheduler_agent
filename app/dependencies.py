from fastapi import Depends, Header, HTTPException
from app.config import settings

def get_api_key(x_api_key: str = Header(...)):
    """
    Dependency to validate incoming requests with an API key.
    """
    if x_api_key != settings.SCALEDOWN_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key

def get_current_user(user_id: str = Header(None)):
    """
    Dependency to simulate user authentication.
    In real implementation, integrate with OAuth2 / JWT.
    """
    if not user_id:
        raise HTTPException(status_code=401, detail="User ID header missing")
    return {"user_id": user_id}