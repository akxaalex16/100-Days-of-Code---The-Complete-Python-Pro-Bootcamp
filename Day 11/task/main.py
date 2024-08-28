import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
if_play = True
user_cards = []
computer_cards = []
def deal_card():
    return
def calculate_score(cards_list):
    return cards_list


while if_play:
    play_yes_or_no = input("Do you want to play a game of Blackjack? Tpe 'y' or 'n': ")
    if play_yes_or_no == 'y':
        print(logo)
        your_cards = random.choices(cards, k=2)
        your_score = sum(your_cards)
        dealer_card = random.choice(cards)
        print(f"Your cards: {your_cards}, current score: {your_score}  ")
        print(f"Computer's first card: {dealer_card}")
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_another_card == 'y':
            your_other_card = random.choice(cards)
            score_now = your_cards + your_other_card
            print(f"Your cards: {your_cards, your_other_card}, current score: {score_now}")
            print(f"Computer's first card: {dealer_card}")

