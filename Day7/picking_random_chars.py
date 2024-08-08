import random

word_list = ['aardvark', 'baboon', 'camel']
letter_list = ['']
print('Welcome to Hangman')


# Randomly choose a word for the word_list and assign it
chosen_word = random.choice(word_list)
print(chosen_word)

# Ask the user to guess a letter and assign their 
user_letter = input('Please guess a letter:\n')
user_letter = user_letter.lower()
print(user_letter)


# Check if the letter the user guess is right or wrong
for letter in user_letter:
    if letter == user_letter:
        print('Test')
    else:
        print('Test2')