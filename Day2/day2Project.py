#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator")
bill = input("What was the total bill?\n")
bill = float(bill)
tip = input("How much tip would you like to give? 10, 12 or 15 percent?\n")
tip = int(tip)
tip = tip / 100 + 1
people = input("How many people split the bill?\n")
people = int(people)

#Each person should pay (150.00 / 5) * 1.12 = 33.6
amount = round((bill/people) * tip, 2)
print(amount) 