# a <= range(a, b) < b

# the range function has a step of 1,
# if we want to increase by any other number we do this
for number in range(1, 11, 3):
    print(number)

total = 0
for num in range(1, 101):
    total += num

print(total)
