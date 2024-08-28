import random
from art import logo

if_play = True


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    single_card = random.choice(cards)
    return single_card


user_cards = []
computer_cards = []

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    # user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(cards):
    # if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)


while if_play:
    play_yes_or_no = input("Do you want to play a game of Blackjack? Tpe 'y' or 'n': ")
    if play_yes_or_no == 'y':
        print(logo)



