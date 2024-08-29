from art import logo
import random

# choose a random number between 1-100
# function to set difficulty
# let the user guess a number
# function to check users' guess against actual answer
# track number of attempts and reduce by 1 if they get it wrong
# repeat the guessing functionality if they get it wrong


EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")


def set_difficulty():
    difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_type == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def game():
    print(logo)
    random_number = random.randint(1, 100)
    print(f"Welcome to the number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {random_number}.")

    turns = set_difficulty()

    guesses = 0
    while guesses != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guesses = int(input("Make a guess: "))
        turns = check_answer(guesses, random_number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guesses != random_number:
            print("Guess again.")


game()


