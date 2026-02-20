from app.agents.optimizer import optimize_schedule
from app.demo.demo_data import demo_meetings

def run_demo_optimize():
    result = optimize_schedule(demo_meetings)
    print("Demo Optimized Schedule:", result)

if __name__ == "__main__":
    run_demo_optimize()