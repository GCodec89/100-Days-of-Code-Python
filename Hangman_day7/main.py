import random

from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

# set lives = 6
lives = 6

# art vars
len_art = len(stages)

# program chooses a random word
len_list = len(word_list)
word_index = random.randint(1, len_list)
word = word_list[word_index - 1]
#print(word)

#creates placeholder for user to see
placeholder = ""
len_word = len(word)
while len_word > 0:
    placeholder += "_"
    len_word -= 1
print(f"Word to guess: {placeholder}")

# 1st input for user
guess = input("Guess a letter: ").lower()

# aux display
display = ["_"] * len(word)

# game_over is set to False
game_over = False

# list of correct letters and wrong letters
correct_letter = []
wrong_letter = []

while not game_over:

    # resets aux vars
    len_word = len(word)
    i = 0
    j = 0

    # handles display
    # handles "Letter already guessed."
    # add letter to list correct_letter
    # j is a counter and is not 0 if guess is in word
    while len_word > 0:
        if word[i] == guess:
            display[i] = word[i]
            j += 1
            if guess in correct_letter and j == 1:
                print("Letter already guessed.")
            if guess not in correct_letter:
                correct_letter.append(guess)
        len_word -= 1
        i += 1

    # j is 0 if guess is not in word
    # handles new wrong letters, and repeated wrong letters
    # handles end game
    if j == 0:
        lives -= 1
        if guess in wrong_letter:
            print(f"You guessed {guess}, again... It's still not in the word. You loose a life!, again...")
        if guess not in wrong_letter:
            wrong_letter.append(guess)
            print(f"You guessed {guess}, that's not in the word. You loose a life!")
        if lives == 0:
            game_over = True
            print("You loose!")

    # prints that guess is correct
    if j != 0 and guess not in correct_letter:
        print("You guessed correctly!")

    # prints hangman_art stages
    print(f"{stages[lives]}")

    #prints number of lives left
    if lives > 0 and "_" in display:
        print(f"**************** You still have {lives} lives *************")

    # prints list of letters guessed
    if lives != 0 and "_" in display:
        print(f"Letters guessed -> Correct letters: {correct_letter} Wrong letter: {wrong_letter}")

    # prints display
    if lives > 0 and "_" in display:
        print(f"Word to guess: {"".join(display)}")

    # new input to user
    if "_" in display and lives > 0:
        guess = input("Guess a letter: ").lower()

    # You win
    if "_" not in display:
        game_over = True
        print(f"You got it! the right word is: {word}\n**************** You win! ****************")

    # last message that tells word if you loose
    if game_over == True and lives == 0:
        print(f"************** The right word was {word}. Try again! **************")
