import requests

BASE_URL = "http://127.0.0.1:8000"
HEADERS = {"x-api-key": "NNZjxqB7PS9tkdrm3aB7W8eyedBMazm08T7nkJ5k", "user_id": "u1"}

def run_demo():
    # 1. Create user
    user = {
        "id": "u1",
        "name": "Jithinvas",
        "preferences": {"preferred_times": ["morning", "afternoon"]}
    }
    print("Create User:", requests.post(f"{BASE_URL}/user/create", json=user).json())

    # 2. Schedule meeting
    meeting = {
        "id": "m1",
        "title": "Team Sync",
        "start": "2026-02-21T10:00:00",
        "end": "2026-02-21T11:00:00"
    }
    print("Schedule Meeting:", requests.post(f"{BASE_URL}/schedule/create", json=meeting).json())

    # 3. Optimize meetings
    meetings = [meeting, {
        "id": "m2",
        "title": "Project Review",
        "start": "2026-02-21T10:30:00",
        "end": "2026-02-21T11:30:00"
    }]
    print("Optimize:", requests.post(f"{BASE_URL}/optimize/", json=meetings).json())

    # 4. Analytics
    analytics = {
        "user_id": "u1",
        "total_meetings": 5,
        "cancelled_meetings": 1,
        "average_duration_minutes": 45,
        "preferred_times": ["morning", "afternoon"]
    }
    print("Analytics:", requests.post(f"{BASE_URL}/analytics/", json=analytics).json())

    # 5. Secure endpoint
    print("Secure Data:", requests.get(f"{BASE_URL}/secure/secure-data", headers=HEADERS).json())

if __name__ == "__main__":
    run_demo()