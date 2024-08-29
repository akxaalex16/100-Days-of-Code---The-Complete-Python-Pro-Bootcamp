# there is no block scope in python

if 3 > 2:
    a_var = 10
#   accessible anywhere

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
