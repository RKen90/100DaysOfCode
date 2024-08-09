'''
Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, 
if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

**Warning** The function must be called life_in_weeks for the tests to pass. Also the output must have the same punctuation and spelling as the example. Including the full stop!

Example Input
56
Example Output
You have 1768 weeks left.
'''

def age_in_weeks(name, age):
    age_w = age * 52
    age90 = 90 * 52
    weeks_left = age90 - age_w
    print(f"Hello {name}, you have lived for {age_w} weeks, you have {weeks_left} weeks left")
    
age_in_weeks("Robert", 34)
age_in_weeks("Mirna", 32)