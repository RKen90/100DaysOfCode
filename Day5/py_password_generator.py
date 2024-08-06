#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create placeholder blank password
password = []

# for loop for nr_letters
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char
    print(password)
    
# for loop for nr_symbols
for symb in range(1, nr_symbols + 1):
    random_symb = random.choice(symbols)
    password += random_symb
    print(password)

for num in range(1, nr_numbers + 1):
    random_numb = random.choice(numbers)
    password += random_numb
    print(password)

# random.shuffle shuffling the list
random.shuffle(password)
print(f'The password list is {password}')


new_pass = ""
for i in password:
    new_pass += i
    print(new_pass)
print(f'Your password is {new_pass}')
    

'''
legging (gry/planes/black)
sportsbra (teehee)
panties
sports shoe
sock
hair scrunchies (bathroom)
'''

