# Initial state setup
current_state = ['A', 1, 'B', 1]  # Initial state with both rooms dirty
goal_state = ['A', 0, 'B', 0]      # Goal state (both rooms clean)
total_cost = 0                      # Initialize total cost

def print_status():
    print(f"Current state: {current_state}")
    print(f"Vacuum is placed in Location {position}")
    print(f"Total cleaning cost so far: {total_cost}")

def check_and_clean(start_room):
    process_room(start_room, current_state[current_state.index(start_room) + 1])
    other_room = 'B' if start_room == 'A' else 'A'
    process_room(other_room, current_state[current_state.index(other_room) + 1])
    check_goal_state()

def process_room(room, status):
    if status == 1:
        clean_room(room)
    else:
        print(f"Location {room} is already clean.")

def clean_room(room):
    global total_cost
    print(f"Location {room} is Dirty.")
    current_state[current_state.index(room) + 1] = 0  # Set status to 0 (cleaned)
    print(f"Location {room} has been Cleaned.")

    # Increase total cost for cleaning
    cost_of_cleaning = 1  # Define the cost for each cleaning operation
    total_cost += cost_of_cleaning
    print(f"COST for SUCK at Location {room}: {cost_of_cleaning}")

    # Move the vacuum to the next room after cleaning
    move_to_next_room(room)
    print_status()

def move_to_next_room(room):
    global position
    if room == 'A':
        position = 'B'
        print(f"Moving right to Location B.")
    elif room == 'B':
        position = 'A'
        print(f"Moving left to Location A.")

def check_goal_state():
    if current_state == goal_state:
        print("Final goal state reached:", goal_state)
    else:
        print("Goal state not yet reached.")

def get_room_status():
    for room in ['A', 'B']:
        status = input(f"Is location {room} dirty? (yes/no): ").strip().lower()
        if status == 'yes':
            current_state[current_state.index(room) + 1] = 1  # Set status to 1 (dirty)
        elif status == 'no':
            current_state[current_state.index(room) + 1] = 0  # Set status to 0 (clean)
        else:
            print("Invalid input. Assuming the room is clean.")
            current_state[current_state.index(room) + 1] = 0  # Default to clean

if __name__ == "__main__":
    position = input("Which room do you want to start cleaning? (A/B): ").strip().upper()

    if position in ['A', 'B']:
        get_room_status()  # Ask user for the status of each room
        print_status()
        check_and_clean(position)
    else:
        print("Invalid choice. Please restart and choose either A or B.")
