"""
High-Low Game
A game where the user is given a randomly generated number betweeen 1 and 100,
and then guesses whether their number is higher or lower than the computer.
A scored is recorded based on the number of times the user is correct.

"""

import random

# Constant which defines the number of rounds in the game
ROUND_LIMIT = 5

# Dictionary which records the round number and current user score
game_state = {
"round_number": 1,
"current_score": 0
}

def main():
    
    # Prints a welcome message
    print("Welcome to the High-Low Game!")
    print("----------------------------")
    print("Round:", game_state["round_number"])

    # Calculates a random integer between 1 and 100 for the user and the computer
    your_number = random.randint(1,100)
    computer_number = random.randint(1,100)

    # The user is told their number...
    print("Your number is:", your_number)
    # ...and is prompted to guess whether it beats the computer number (hidden).
    your_guess = input("Do you think your number is higher or lower than the computer?")

    # Checks the user guess and number and computer numbers against each other and provides various outcomes
    # If user guess was higher and user number is higher:
    if your_guess == "higher" and your_number > computer_number:
        print("You were correct! The computer's number was:", computer_number)
        # Increases round number and score by one and prints score
        game_state["round_number"] += 1
        game_state["current_score"] += 1
        print("Your score is:", game_state["current_score"])
    # If user guess was lower and user number is lower:
    elif your_guess == "lower" and computer_number > your_number:
        print("You were correct! The computer's number was:", computer_number)
        # Increases round number and score by one and prints score
        game_state["round_number"] += 1
        game_state["current_score"] += 1
        print("Your score is:", game_state["current_score"])
    # If user guess was higher and user number is lower:
    elif your_guess ==  "higher" and computer_number > your_number:
        print("You were wrong! The computer's number was:", computer_number)
        # Increases round number by one and prints score
        game_state["round_number"] += 1
        print("Your score is:", game_state["current_score"])
    # If user guess was lower and user number is higher:
    elif your_guess ==  "lower" and your_number > computer_number:
        print("You were wrong! The computer's number was:", computer_number)
        # Increases round number by one and prints score
        game_state["round_number"] += 1
        print("Your score is:", game_state["current_score"])
    # If user number was tied with computer number
    else:
        print("Tie! The computer's number was:", computer_number)
        # Increases round number by one and prints score
        game_state["round_number"] += 1
        print("Your score is:", game_state["current_score"])


if __name__ == "__main__":
    main()
