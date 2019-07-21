import random

print("Hello, welcome to hangman!")
name = input("What is your name?")
print("Hello, {}".format(name))
game = input("Would you like to continue? Type Y for yes and N for no")
if game == "N":
    exit()

words = ['good morning', 'python']
chosen_word = random.choice(words)

num_letters = len(chosen_word)
for i in range(0, len(chosen_word)):
    print("_")

guess_letters = input("Guess a letter in the word. Type the letter here: ")
while chosen_word == "good morning":
    if guess_letters in (chosen_word):
        print("Correct!")
    else:
        input("Incorrect! Try again!")
    continue

while chosen_word == "python":
    if guess_letters in (chosen_word):
        print("Correct!")
    else:
        input("Incorrect! Try again!")
    continue
