# lottery game 

import random

def generate_winning_numbers(num_choices, num_draws):
    """Generate a list of random numbers from 1 to 49, with no repeats."""
    
    return random.sample(range(1, num_choices + 1), num_draws)

def get_user_numbers(num_choices, num_draws):
    
    print(f"Choose {num_draws} numbers between 1 and {num_choices}:")
    user_numbers = []
    while len(user_numbers) < num_draws:
        try:
            user_input = int(input(f"Enter number {len(user_numbers) + 1}: "))
            if 1 <= user_input <= num_choices and user_input not in user_numbers:
                user_numbers.append(user_input)
            else:
                print("Invalid input. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return user_numbers

def check_winning(user_numbers, winning_numbers):
    
    return len(set(user_numbers) & set(winning_numbers))

def main():
    num_choices = 19 # Total available choices (e.g., 1 to 19)
    num_draws = 6     # Number of winning numbers to draw

    winning_numbers = generate_winning_numbers(num_choices, num_draws)
    user_numbers = get_user_numbers(num_choices, num_draws)

    matching_count = check_winning(user_numbers, winning_numbers)

    print(f"Winning numbers: {winning_numbers}")
    print(f"Your chosen numbers: {user_numbers}")
    print(f"Matching numbers: {matching_count}")

    # Calculate chances of winning
    total_possible_combinations = 1
    for i in range(num_draws):
        total_possible_combinations *= (num_choices - i)
    chances_of_winning = 1 / (total_possible_combinations // (num_draws * (num_draws - 1)))

    print(f"Chances of winning: {chances_of_winning:.10f}")
    print("Better luck next time")
if __name__ == "__main__":
    main()
