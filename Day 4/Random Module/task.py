import random
import my_module

# random.randint(a,b)
# returns a random int N such that a <= N <= b

# random whole numbers within a range
random_integer = random.randint(1, 10)
print(random_integer)

# modules in python
print(my_module.my_fav_number)

# random floats 0-1
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# random floats
random_float = random.uniform(1, 10)
print(random_float)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print('Heads')
else:
    print('Tails')



