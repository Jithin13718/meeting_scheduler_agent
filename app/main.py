from fastapi import FastAPI
from app.routers import schedule, optimize, analytics, auth, user, secure

app = FastAPI(
    title="Meeting Scheduler Agent",
    description="Intelligent scheduling system with conflict resolution and optimization",
    version="1.0.0"
)

app.include_router(schedule.router, prefix="/schedule", tags=["Schedule"])
app.include_router(optimize.router, prefix="/optimize", tags=["Optimize"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(secure.router, prefix="/secure", tags=["Secure"])

@app.get("/")
def read_root():
    return {"message": "Meeting Scheduler Agent API is running"}