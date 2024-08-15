import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# option 1
random_pick = random.choice(friends)
print(random_pick)

# option 2
random_index = random.randint(0, 4)
print(friends[random_index])
