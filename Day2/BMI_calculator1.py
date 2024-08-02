'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
BMI Wikipedia Page
The BMI is a measure of someone's weight taking into account their height. e.g. 
If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.


'''

# 1st input: enter height in meters e.g: 1.65
height = input("What is your height in Meters?\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("What is your weight in KG?\n")
# 🚨 Don't change the code above 👆
height = float(height)
weight = float(weight)

bmi = weight / (height * height)
bmi = int(bmi)
print(bmi)
# Write your code below this line 👇