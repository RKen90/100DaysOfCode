'''
Computers are Deterministic

Machines doing repeatable things

Pseudorandom Number Generators
Python uses the Mersenne Twister Algorithm for randomness
'''

# Using the random module
import random
import my_module

print(random.randint(1, 10))
print(random.randint(1, my_module.my_favourite_number))
print(my_module.my_favourite_number)


# Using random floating point numbers
print(random.random())
print(random.random() * 10)

print(random.uniform(1, 10))