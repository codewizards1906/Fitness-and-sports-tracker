# Fitness and Sports Tracker
# Made for STEM students

import datetime

# Store fitness data
fitness_data = []

# Function to add new activity
def add_activity():
    name = input("Enter your name: ")
    activity = input("Enter activity (e.g., running, cycling, yoga): ")
    minutes = int(input("Enter duration in minutes: "))
    steps = int(input("Enter steps taken (if any): "))

    # Simple calories formula
    calories = minutes * 5  # approx 5 calories per minute
    date = datetime.date.today()

    # Save data
    record = {
        "name": name,
        "activity": activity,
        "minutes": minutes,
        "steps": steps,
        "calories": calories,
        "date": str(date)
    }
    fitness_data.append(record)
    print("\n✅ Activity added successfully!\n")

# Function to show all activities
def show_summary():
    if not fitness_data:
        print("No data available yet. Add an activity first!")
        return

    print("\n📊 Fitness Summary:\n")
    total_steps = 0
    total_calories = 0
    for record in fitness_data:
        print(f"{record['date']} - {record['name']} did {record['activity']} for {record['minutes']} min, "
              f"{record['steps']} steps, {record['calories']} cal")
        total_steps += record['steps']
        total_calories += record['calories']

    print("\n🏁 Total Steps:", total_steps)
    print("🔥 Total Calories Burned:", total_calories)

# Function to show menu
def menu():
    while True:
        print("\n=== FITNESS AND SPORTS TRACKER ===")
        print("1. Add Activity")
        print("2. Show Summary")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_activity()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("Goodbye! Stay fit and active 💪")
            break
        else:
            print("Invalid choice. Try again!")

# Run program
menu()