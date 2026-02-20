# Meeting Scheduler Agent

An intelligent scheduling system built with **FastAPI** that supports:
- User creation and preference learning
- Meeting scheduling
- Conflict resolution and optimization
- Analytics
- Secure access with API key authentication

## 🚀 Features
- **User Management**: Create users with preferences
- **Scheduling**: Add meetings with participants
- **Optimization**: Resolve conflicts and optimize schedules
- **Analytics**: Track meeting statistics
- **Secure Endpoints**: API key + user authentication

---

## 📦 Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/meeting_scheduler_Agent.git
cd meeting_scheduler_Agent
pip install -r requirements.txt

Create a .env file in the project root:
SCALEDOWN_API_KEY=your_api_key_here

Run the server:
uvicorn app.main:app --reload

Swagger UI will be available at:
http://127.0.0.1:8000/docs

## working of agent
## Screenshots
![Screenshot 223706](docs/screenshots/Screenshot%202026-02-20%20223706.png)
![Screenshot 223928](docs/screenshots/Screenshot%202026-02-20%20223928.png)
![Screenshot 223947](docs/screenshots/Screenshot%202026-02-20%20223947.png)
![Screenshot 224005](docs/screenshots/Screenshot%202026-02-20%20224005.png)
![Screenshot 224035](docs/screenshots/Screenshot%202026-02-20%20224035.png)
![Screenshot 224047](docs/screenshots/Screenshot%202026-02-20%20224047.png)
![Screenshot 224057](docs/screenshots/Screenshot%202026-02-20%20224057.png)

