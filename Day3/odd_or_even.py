'''
Instructions
Write a program that works out whether if a given number is an odd or even number.
Even numbers can be divided by 2 with no remainder.
e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.
e.g. 59 is odd because 59 ÷ 2 = 29.5
29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example 1 Input
43
Example 1 Output
This is an odd number.
Example 2 Input
94
'''

print("Welcome to the Odd or Even Machine!")
number = input("Please enter your number\n")
number = int(number)

if number % 2 == 0:
    print("Your number is even")
elif number % 2 != 0:
    print("Your number is odd!")
else:
    print("Please try another number") 

