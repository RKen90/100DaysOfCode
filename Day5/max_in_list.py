# Create a function that will pick out the largest function in a list
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
highest = 0
checking = 0

for score in student_scores:
    checking = score
    if checking > highest:
        highest = checking
        print(highest)
print(f'The Highest number in the list is {highest}')

student_scores.append(246)

for score in student_scores:
    checking = score
    if checking > highest:
        highest = checking
        print(highest)
print(f'The Highest number in the list is {highest}')