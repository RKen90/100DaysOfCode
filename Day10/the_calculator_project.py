calculator = '''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | ÷ | |
| |___|___|___| |___| |
|_____________________|

'''

print(calculator)
# Gathering Inputs 
print("Welcome to the calculator program!")

f_num = float(input("What is your first number?\n"))
carry_on = True  # Initialize the loop control variable

# Defining operations for calculator
def add(f_num, s_num):
    return f_num + s_num

def subtract(f_num, s_num):
    return f_num - s_num

def multiply(f_num, s_num):
    return f_num * s_num

def divide(f_num, s_num):
    return f_num / s_num

# Start the calculation loop
while carry_on:
    operator = input('''
+
-
*
/                 
Pick an operation\n''')
    s_num = float(input("What is your second number?\n"))

    # Defining logic for calculator 
    if operator == "+":
        calc = add(f_num, s_num)
    elif operator == "-":
        calc = subtract(f_num, s_num)
    elif operator == "*":
        calc = multiply(f_num, s_num)
    elif operator == "/":
        calc = divide(f_num, s_num)
    else:
        print("Please enter a valid operator")
        continue  # Skip to the next loop iteration if an invalid operator is entered

    print(f"The current calculation is {calc}")

    # Continue the calculation?
    continue_calc = input("Do you wish to continue the calculation? Y or N\n")
    if continue_calc.lower() == "n":
        carry_on = False
    else:
        # Set f_num to the result of the last calculation to continue the process
        f_num = calc

print("Thank you for using the calculator!")
