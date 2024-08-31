from art import logo, vs
from game_data import data
import random

# display art
# generate a random account from the game data
# format the account data into printable format
# ask user for a guess on who has more followers
# check if user is correct
# #      get follower count of each account
# #      write if statement to check if user is correct
# give user feedback on their guess
# score keeping
# make the game repeatable if they get it correct
# make the account at position B become the next account at position A
# clear the console after the user guess


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_description}, from {account_country}.'


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and return if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
        # another option
        # if user_guess == 'a':
        #     return True
        # else:
        #     return False


print(logo)

score = 0

game_should_continue = True

choice_B = random.choice(data)

while game_should_continue:
    choice_A = choice_B
    choice_B = random.choice(data)
    # choice_A = random.choice(data)
    # choice_B = random.choice(data)
    while choice_A == choice_B:
        choice_B = random.choice(data)

    print(f"Compare A: {format_data(choice_A)}")
    print(vs)
    print(f"Against B: {format_data(choice_B)}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = choice_A["follower_count"]
    b_follower_count = choice_B["follower_count"]

    is_correct = check_answer(choice, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f'You are correct! Current score: {score}')
    else:
        print(f"Sorry, that is wrong. Final score: {score}")
        game_should_continue = False

