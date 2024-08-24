from art import logo

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(logo)


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f'The winner is {winner} with a bid of ${highest_bid}.')


name_and_bid = {}
continue_bidding = True

while continue_bidding:
    name = input('What is your name? ')
    bid = int(input('What is your bid? $ '))
    name_and_bid[name] = bid
    other_users = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if other_users == "no":
        continue_bidding = False
        find_highest_bidder(name_and_bid)
    elif other_users == "yes":
        print("\n" * 100)



