from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_optimize_schedule():
    payload = [
        {
            "title": "Meeting A",
            "start_time": "2026-02-21T09:00:00",
            "end_time": "2026-02-21T10:00:00",
            "participants": ["alice@example.com"]
        },
        {
            "title": "Meeting B",
            "start_time": "2026-02-21T09:30:00",
            "end_time": "2026-02-21T10:30:00",
            "participants": ["bob@example.com"]
        }
    ]
    response = client.post("/optimize/", json=payload)
    assert response.status_code == 200
    assert "optimized_schedule" in response.json()