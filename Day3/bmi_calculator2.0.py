'''
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
'''

print("Welcome to the BMI Calculator FatAss!")
height = float(input("Please enter your height in M\n"))
weight = int(input("Please enter your weight in KG\n"))

bmi = round(weight / (height * height), 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}. Eat a burger skinny!")
elif bmi<25:
    print(f"Your BMI is {bmi}.You are a normal weight, good job!")
elif bmi <30:
    print(f"Your BMI is {bmi}.You are slightly overweight")
elif bmi <35:
    print(f"Your BMI is {bmi}.You are obese fatty!")
else:
    print(f"Your BMI is {bmi}.You are clinically obese, lose some weight before you drop dead!") 