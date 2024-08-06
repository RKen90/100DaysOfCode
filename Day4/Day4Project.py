import random

print("Welcome to the Rock, Paper, Scissors Simulator!")
user_choice = input("Rock, Paper or Scissors? 1 for Rock, 2 for Scissors, 3 for Paper\n")
user_choice = int(user_choice)

'''
Rock wins against scissors
Scissors wins against paper
Paper wins against rock
'''

ascii_art = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,  # Rock (index 0)
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """,  # Scissors (index 1)
    """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """  # Paper (index 2)
]

computer_choice = random.randint(1, 3)
#print(computer_choice)

# User Choice for Rock
if user_choice == 1:
    print(ascii_art[0])
    if computer_choice == 1:
        print(ascii_art[0])
        print('Draw')
    elif computer_choice == 2:
        print(ascii_art[1])
        print('Player 1 Wins')
    else:
        print(ascii_art[2])
        print('Computer Wins')
# User choice for Scissors
elif user_choice == 2:
    print(ascii_art[1])
    if computer_choice == 1:
        print(ascii_art[0])
        print('Computer Wins')
    elif computer_choice == 2:
        print(ascii_art[1])
        print('Draw')
    else:
        print(ascii_art[2])
        print('Player 1 Wins')

# User choice for Paper
elif user_choice == 3:
    print(ascii_art[2])
    if computer_choice == 1:
        print(ascii_art[0])
        print('Player 1 Wins')
    elif computer_choice == 2:
        print(ascii_art[1])
        print('Computer Wins')
    else:
        print(ascii_art[2])
        print('Draw')
else:
    print('Not a number, please try again!')