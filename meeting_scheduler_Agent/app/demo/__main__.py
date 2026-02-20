import sys
from . import demo_schedule, demo_optimize, demo_user

def main():
    print("=== Demo Runner ===")
    print("1. Run Schedule Demo")
    print("2. Run Optimize Demo")
    print("3. Run User Preferences Demo")
    choice = input("Select a demo (1-3): ")

    if choice == "1":
        demo_schedule.run_demo_schedule()
    elif choice == "2":
        demo_optimize.run_demo_optimize()
    elif choice == "3":
        demo_user.run_demo_user()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()