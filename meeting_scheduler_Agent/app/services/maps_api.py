from app.config import settings

def get_travel_time(origin: str, destination: str) -> dict:
    """
    Placeholder for Google Maps Distance Matrix API.
    If MAPS_API_KEY is missing, return a safe fallback.
    """
    if not settings.MAPS_API_KEY:
        return {"warning": "MAPS_API_KEY not configured", "travel_time_minutes": None}

    # Placeholder response (replace with real API call later)
    return {"origin": origin, "destination": destination, "travel_time_minutes": 25}