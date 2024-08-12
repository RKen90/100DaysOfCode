'''
Dictionaries
Key/Value Pairs
- Key: A word
- Value: The meaning associated with the word

Bug - An errior in a program that prevents the program from running as expected

{Key: Value}
'''

# Declaring a dictionary
programming_dictionary = {"Bug": " An error in a program that prevents the program from running as expected",
 "Function": "A piece of code that you can easily call over and over again"}

# Retrieving items from a dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Adding info to a dictionary after defining it
programming_dictionary["Loop"] = "The Action of doing something over and over again"
print(programming_dictionary["Loop"])

# Wiping a dictionary
#programming_dictionary = {}

# Editing an item in a dictionary
print(programming_dictionary["Bug"])
programming_dictionary["Bug"] = "A Moth in your computer"
print(programming_dictionary["Bug"])

# Looping through a dictionary
for i in programming_dictionary:
    print(programming_dictionary, programming_dictionary[i])