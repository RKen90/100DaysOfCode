employee_scores = {
    "Alice": 92,
    "Bob": 88,
    "Charlie": 79,
    "Diana": 95,
    "Eve": 62,
    "Frank": 58,
}

employee_ratings = {}

for employee in employee_scores:
    score = employee_scores[employee]
    
    if score >= 95:
            employee_ratings[employee] = 'Excellent'
    elif score >= 85:
        employee_ratings[employee] = 'Very Good'
    elif score >= 75:
        employee_ratings[employee] = 'Good'
    elif score >=60:
        employee_ratings[employee] = 'Satisfactory'
    else:
        employee_ratings[employee] = 'Needs Improvement'
        
print(employee_ratings["Frank"])
