student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
total_score = 0

print(sum(student_scores))

for score in student_scores:
    total_score += score
    print(total_score)
print(f'The total score was {total_score}')

