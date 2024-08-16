student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# sum of values in a list
total_exam_scores = sum(student_scores)
print(total_exam_scores)

adding = 0
for score in student_scores:
    adding += score

print(adding)

# max value in a list
print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)


# practice
exam_grade = [8, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for i in exam_grade:
    if i > highest_score:
        highest_score = i

print(highest_score)