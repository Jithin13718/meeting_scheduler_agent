# API Endpoints

This document describes the available endpoints in the Meeting Scheduler Agent.

## User
- **POST /user/create**  
  Create a new user.  
  **Body Example:**
  ```json
  {
    "id": "u1",
    "name": "Jithinvas",
    "email": "jithinvas@example.com",
    "preferences": {
      "preferred_times": ["morning", "afternoon"]
    }
  }
