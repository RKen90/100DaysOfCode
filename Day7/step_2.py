import random

word_list = ['aardvark', 'baboon', 'camel']
letter_list = ['']
print('Welcome to Hangman')


# Randomly choose a word for the word_list and assign it
chosen_word = random.choice(word_list)
print(chosen_word)

solution = ""
for letter in chosen_word:
    solution += '_'
print(solution)

# Ask the user to guess a letter and assign their 
user_letter = input('Please guess a letter:\n')
user_letter = user_letter.lower()
print(user_letter)

        
# Put the guessed letter into the right position
display = ''

# Check if the letter the user guess is right or wrong
for letter in chosen_word:
    if letter == user_letter:
        display += letter
    else:
        display += "_"
        
print(display)