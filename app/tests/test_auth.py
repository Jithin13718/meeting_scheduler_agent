from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_auth_callback():
    response = client.get("/auth/callback?code=test123")
    assert response.status_code == 200
    assert response.json()["code"] == "test123"