# Setting up student score dictionary

student_score = {
    "Catherine": 97,
    "David": 76,
    "Katy": 84,
    "Mirna": 90,
    "The Tim": 70,
    "James": 86,
}

# Creating a new dictionary student_grades
student_grades = {}

# Looping through existing dictionary, taking names and adding them to student_grades
for student in student_score:
    score = student_score[student]
    
    if score >= 91:
            student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
        
print(student_grades['Mirna'])