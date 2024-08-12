# Setting up a dictionaty with fake student scores

student_scores = {
    "Amr": 91,
    "Nadine": 97,
    "Geoff": 64, 
    "Nate": 14,
    "Mikel": 77,
    "Storm": 97,
}

# Step 1 Taking the names and adding them to the new dictionary student_grades
student_grades = {}

for student in student_scores:
        #Get the value (student score) by using the key each time.
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
        
print(student_grades['Nate'])