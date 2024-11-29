"""
High-Low Game
A game where the user is given a randomly generated number betweeen 1 and 100,
and then guesses whether their number is higher or lower than the computer's.
A point is scored if the user guesses correctly, otherwise the computer scores a point instead.
Once the score limit has been reached by either party, the game ends and a winner is declared.
"""

import random

# Constants which define the range for the random integers to be calculated
LOWEST_ROLL = 1
HIGHEST_ROLL = 100

# Constant which defines the maximum score in the game before it ends
SCORE_LIMIT= 3

def main():
    # Dictionary which records the round number, user score and computer score
    game_state = {
    "round_number": 1,
    "user_score": 0,
    "computer_score": 0
    }

    # Prints a welcome message
    print(end='\n')
    print("Welcome to the High-Low Game!")
    print("----------------------------")
    print(end='\n')
    
    # Loops the game until a score limit is met 
    while game_state["user_score"] <SCORE_LIMIT and game_state["computer_score"]<SCORE_LIMIT:
        print("Round:", game_state["round_number"])
        print(end='\n')

        # Calculates a random integer between 1 and 100 for the user and the computer
        your_number = random.randint(LOWEST_ROLL,HIGHEST_ROLL)
        computer_number = random.randint(LOWEST_ROLL,HIGHEST_ROLL)

        # The user is told their number...
        print("Your number is:", your_number)
        print(end='\n')
        # ...and is prompted to guess whether it beats the computer number (hidden).
        your_guess = input("Do you think your number is higher or lower than the computer?")
        print(end='\n')

        # Checks the user guess and number and computer numbers against each other and provides various outcomes
        # If user guess was higher and user number is higher:
        if your_guess == "higher" and your_number > computer_number:
            print("You were correct! The computer's number was:", computer_number)
            print(end='\n')
            # Increases round number and score by one and prints scores
            game_state["round_number"] += 1
            game_state["user_score"] += 1
            print("Your score is:", game_state["user_score"])
            print("Computer score is:", game_state["computer_score"])
            print(end='\n')
        # If user guess was lower and user number is lower:
        elif your_guess == "lower" and computer_number > your_number:
            print("You were correct! The computer's number was:", computer_number)
            print(end='\n')
            # Increases round number and score by one and prints scores
            game_state["round_number"] += 1
            game_state["user_score"] += 1
            print("Your score is:", game_state["user_score"])
            print("Computer score is:", game_state["computer_score"])
            print(end='\n')
        # If user guess was higher and user number is lower:
        elif your_guess ==  "higher" and computer_number > your_number:
            print("You were wrong! The computer's number was:", computer_number)
            print(end='\n')
            # Increases round number and computer score by one and prints scores
            game_state["round_number"] += 1
            game_state["computer_score"] += 1
            print("Your score is:", game_state["user_score"])
            print("Computer score is:", game_state["computer_score"])
            print(end='\n')
        # If user guess was lower and user number is higher:
        elif your_guess ==  "lower" and your_number > computer_number:
            print("You were wrong! The computer's number was:", computer_number)
            print(end='\n')
            # Increases round number and computer score by one and prints scores
            game_state["round_number"] += 1
            game_state["computer_score"] += 1
            print("Your score is:", game_state["user_score"])
            print("Computer score is:", game_state["computer_score"])
            print(end='\n')
        # If user number was tied with computer number:
        else:
            print("Tie! The computer's number was also:", computer_number)
            print(end='\n')
            # Increases round number by one and prints scores
            game_state["round_number"] += 1
            print("Your score is:", game_state["user_score"])
            print("Computer score is:", game_state["computer_score"])
            print(end='\n')

    if game_state["user_score"]>=SCORE_LIMIT:
        print("Congratulations! You beat the computer.")
    elif game_state["computer_score"]>=SCORE_LIMIT:
        print("Unlucky. The computer beat you.")

if __name__ == "__main__":
    main()
