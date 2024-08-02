'''
Type Error 


num_char = len(input("What is your name?\n"))
print("Your name has " + num_char + " characters.")

'''
num_char = len(input("What is your name?\n"))

print(type("What is your name?"))

# Type conversion
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")


number = "123456"
print(type(number))
number_new = int(number)
print(type(number_new))