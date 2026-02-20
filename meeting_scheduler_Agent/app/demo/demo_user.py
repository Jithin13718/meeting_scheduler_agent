from app.agents.preferences import learn_preferences
from app.demo.demo_data import demo_user

def run_demo_user():
    """
    Run the demo for user preference learning.
    """
    result = learn_preferences(demo_user["preferences"])
    print("Demo User Preferences:", result)

if __name__ == "__main__":
    run_demo_user()