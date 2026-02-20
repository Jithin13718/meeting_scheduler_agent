from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analytics():
    payload = {
        "user_id": "123",
        "total_meetings": 10,
        "cancelled_meetings": 2,
        "average_duration_minutes": 45.0,
        "preferred_times": ["morning", "afternoon"]
    }
    response = client.post("/analytics/", json=payload)
    assert response.status_code == 200
    assert response.json()["user_id"] == "123"