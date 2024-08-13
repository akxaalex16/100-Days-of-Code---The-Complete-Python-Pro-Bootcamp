bmi = 84 / 1.65 ** 2
print(bmi)

# int() converts to whole number, flooring
print(int(bmi))

# round(), if it is .5 and above it rounds up, if below it rounds down
print(round(bmi))

# round() to n decimal places
print(round(bmi, 2))


score = 0
# user scores a point
# instead of score = score + 1
score += 1
print(score)


# f-strings
print(f'Your score is: {score}')
