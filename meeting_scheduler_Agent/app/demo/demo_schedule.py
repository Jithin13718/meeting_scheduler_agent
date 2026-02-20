from app.agents.availability import check_availability
from app.demo.demo_data import demo_meetings

def run_demo_schedule():
    """
    Run the demo for schedule availability.
    """
    result = check_availability(calendar_data={"events": demo_meetings})
    print("Demo Schedule Availability:", result)

if __name__ == "__main__":
    run_demo_schedule()