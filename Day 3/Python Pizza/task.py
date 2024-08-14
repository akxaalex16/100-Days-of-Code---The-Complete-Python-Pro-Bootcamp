print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# price = 0
# if size == "s":
#     price += 15
#     if pepperoni == 'y':
#         price += 2
#     if extra_cheese == 'y':
#         price += 1
# elif size == "m":
#     price += 20
#     if pepperoni == 'y':
#         price += 3
#     if extra_cheese == 'y':
#         price += 1
# elif size == 'l':
#     price += 25
#     if pepperoni == 'y':
#         price += 3
#     if extra_cheese == 'y':
#         price += 1
# else:
#     print('Invalid size.')
#
# print(f'Your final bill is: ${price}')

bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print('You typed the wrong inputs.')

if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is : ${bill}.')
