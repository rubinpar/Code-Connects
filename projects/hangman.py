import random

print("Hello, welcome to hangman!")
name = input("What is your name?")
print("Hello, {}".format(name))
game = input("Would you like to continue? Type Y for yes and N for no")
if game == "N":
    exit()

words = ['wonderful', 'python', 'peppermint']
chosen_word = random.choice(words)
guessed_word = ["_" for letter in chosen_word]
print(guessed_word)

num_letters = len(chosen_word)
for i in range(0, len(chosen_word)):
    print("_")

lives = 7

while True:  # not a good idea... you need to figure out what should be in the
# place of true

    guess_letters = input("Guess a letter in the word. Type the letter here: ")
    if guess_letters in chosen_word:
        print("Correct!")
        # find all the indices of all the guessed word
        indices = [i for i, a in enumerate(chosen_word) if a == guess_letters]
        # update the guessed_word with our guessed letters
        for index in indices:
            guessed_word[index] = guess_letters
        print(guessed_word)

    else:
        input("Incorrect!")
        lives = lives - 1

    if "_" not in guessed_word:
        print("Congratulations! You won!")

    if lives == 0:
        print("You lose!")

# Things to do for this program
# 1. It needs to quit when you guessed all the letters.
#       - How do you know when you've gueseed all the letters?
# 2. What happens if someone guesses the same letter twice?
# 3. How do you limit the number of wrong guesses?
# 4. Write more comments.

# Tic-tac-toe?

# 0123456789
# peppermint
# chosen_word.index(guess_letters)
#
# 0123456789
# Hello, welcome to my world.
#
# find all letters in a word python
