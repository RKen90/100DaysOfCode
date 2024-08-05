# Create a program that either prints Heads or Tails
import random

print("Welcome to the Heads or Tails Machine")

number = random.randint(0, 1)
# testing to see if numbers are consistently 0 or 1
#print(number)

if number == 1:
    print("Heads")
else:
    print("Tails")

