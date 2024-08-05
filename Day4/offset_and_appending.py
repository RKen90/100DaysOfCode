# Python Lists
# A type of data structure

# Stroring grouped pieces of data == Lists []
import my_module

fruits = ['apple', 'banana', my_module.my_favourite_number]
print(fruits)
print(fruits[0])
print(len(fruits))
print(fruits[-1])

# Changing elements in the list
fruits[2] = 'Dates'
print(fruits)

# Adding to the list
# Adding to the end of the list
fruits.append('Peach')
print(fruits)