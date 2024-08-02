'''
Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
'''

# 52 Weeks in a year

age = input("What is your age in years?\n")
age = int(age)

age90 = 90 * 52
ageCurrent = age * 52

weeksRemaining = age90 - ageCurrent
print(f"You have lived for {ageCurrent} weeks")
print(f"You have {weeksRemaining} weeks left")