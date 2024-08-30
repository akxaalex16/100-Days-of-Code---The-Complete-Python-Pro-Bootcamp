from art import logo, vs
from game_data import data
import random

score = 0


def compare():
    if data[0]["follower_count"] > data[1]["follower_count"]:
        return "Your right!"


print(logo)
print(f'Compare A: {data[0]["name"]}, a {data[0]["description"]}, from {data[0]["country"]}')
print(vs)
print(f"Against B: {data[1]["name"]}, a {data[1]["description"]}, from {data[1]["country"]}")
choice = input("Who has more followers? Type 'A' or 'B': ").lower()

if choice == "a":
    right = compare()
    print(right)
    score += 1
    print(f"Current score: {score}")
elif choice == "b":
    pass
else:
    print("Invalid input. Please type 'A' or 'B'.")
