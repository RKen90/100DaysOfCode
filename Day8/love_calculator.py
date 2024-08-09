'''
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  
To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"
T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 
Total = 5 
L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3 
'''
def calculate_love_score(name1, name2):
    print("The love calculator is calculating your score...")

    combined_names = name1 + name2
    lower_names = combined_names.lower()
    t = lower_names.count('t')
    r = lower_names.count('r')
    u = lower_names.count('u')  # Corrected: added .count
    e = lower_names.count('e')  # Corrected: added .count

    first_digit = t + r + u + e

    l = lower_names.count('l')
    o = lower_names.count('o')
    v = lower_names.count('v')
    e = lower_names.count('e')  # No conflict as 'e' is simply re-used
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    if (score < 10) or (score > 90):
        print(f"Your score is {score}. You go together like coke and mentos")
    elif (score >= 40) and (score <= 50):
        print(f"Your score is {score}, you are alright together")
    else:
        print(f"Your score is {score}.")

calculate_love_score("Robert", "Mirna")
calculate_love_score("Catherine", "Chance")