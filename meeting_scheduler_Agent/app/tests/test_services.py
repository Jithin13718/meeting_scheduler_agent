import pytest
from app.services.scaledown import compress_prompt
from app.services.maps_api import get_travel_time

def test_scaledown_compress(monkeypatch):
    def mock_post(*args, **kwargs):
        class MockResponse:
            status_code = 200
            def json(self): return {"compressed": "test"}
        return MockResponse()
    monkeypatch.setattr("requests.post", mock_post)

    result = compress_prompt("context", "prompt")
    assert "compressed" in result

def test_maps_api_fallback():
    result = get_travel_time("A", "B")
    assert "travel_time_minutes" in result