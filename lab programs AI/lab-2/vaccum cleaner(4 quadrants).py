# Initial state setup
current_state = ['A', 1, 'B', 1, 'C', 1, 'D', 1]  # Initial state with all rooms dirty
goal_state = ['A', 0, 'B', 0, 'C', 0, 'D', 0]      # Goal state (all rooms clean)
total_cost = 0                                     # Initialize total cost
position = None                                     # Initial position is not set

def print_status():
    print(f"Current state: {current_state}")
    print(f"Vacuum is placed in Location {position}")
    print(f"Total cleaning cost so far: {total_cost}")

def check_and_clean(start_room):
    process_room(start_room, current_state[current_state.index(start_room) + 1])

    # Check and clean remaining rooms
    for i in range(0, len(current_state), 2):
        room = current_state[i]
        if room != start_room:
            process_room(room, current_state[i + 1])

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

    print_status()

def check_goal_state():
    if current_state == goal_state:
        print("Final goal state reached:", goal_state)
    else:
        print("Goal state not yet reached.")

def get_room_status():
    for room in ['A', 'B', 'C', 'D']:
        status = input(f"Is location {room} dirty? (yes/no): ").strip().lower()
        if status == 'yes':
            current_state[current_state.index(room) + 1] = 1  # Set status to 1 (dirty)
        elif status == 'no':
            current_state[current_state.index(room) + 1] = 0  # Set status to 0 (clean)
        else:
            print("Invalid input. Assuming the room is clean.")
            current_state[current_state.index(room) + 1] = 0  # Default to clean

if __name__ == "__main__":
    position = input("Which room do you want to start cleaning? (A/B/C/D): ").strip().upper()

    if position in ['A', 'B', 'C', 'D']:
        get_room_status()  # Corrected function name
        print_status()
        check_and_clean(position)
    else:
        print("Invalid choice. Please restart and choose either A, B, C, or D.")

