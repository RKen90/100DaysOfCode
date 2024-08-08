import random

word_list = ['aardvark', 'baboon', 'camel']
letter_list = ['']
print('Welcome to Hangman')

lives = 6

# Randomly choose a word for the word_list and assign it
chosen_word = random.choice(word_list)
print(chosen_word)

solution = ""
for letter in chosen_word:
    solution += '_'
print(solution)

game_over = False
correct_letter = []

while not game_over:
    
    # Ask the user to guess a letter and assign their 
    user_letter = input('Please guess a letter:\n').lower()
    print(user_letter)

    # Put the guessed letter into the right position
    display = ''
    
    # Check if the letter the user guessed is right or wrong
    for letter in chosen_word:
        if letter == user_letter:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
            
    if user_letter not in chosen_word:
        lives -= 1
        print(lives)
        if lives == 0:
            game_over = True
            print('You Lose')

    print(display)
    
    # Check if there are no more underscores in the display to declare a win
    if "_" not in display:
        print('You Win')
        game_over = True
