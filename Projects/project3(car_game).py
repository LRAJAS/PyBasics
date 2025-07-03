# project car game 
def get_user_choice():
    
    while True:
        user_input = input("Enter your choice (start, stop, accelerate, or quit): ").lower()
        if user_input in ("start", "stop", "accelerate", "quit"):
            return user_input
        else:
            print("Invalid choice. Please choose start, stop, accelerate, or quit.")

def determine_winner(user_speed):
    
    if user_speed >= 80:
        return "You broke the speed limit! Game over."
    elif user_speed >= 50:
        return "Congratulations! You completed the game without breaking the car."
    else:
        return "Your speed is too low. Keep accelerating!"

def play_game():
    
    user_speed = 0
    total_distance = 0
    total_chances = 4  # Updated to 4 chances

    print("Welcome to the Car Speed Game!")
    print("You start with a speed of 0 km/h.")

    while total_distance < 5 and total_chances > 0:
        user_choice = get_user_choice()

        if user_choice == "start":
            print("Car started... Ready to go!")
        elif user_choice == "stop":
            print("Car stopped.")
            user_speed -= 10
        elif user_choice == "accelerate":
            user_speed += 20
            print(f"Accelerated! Current speed: {user_speed} km/h")
        elif user_choice == "quit":
            print("Game stopped.")
            break

        total_distance += 1
        total_chances -= 1

    print(determine_winner(user_speed))

# Start the game
play_game()
