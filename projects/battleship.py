print("Hello! Welcome to Battleship! I'm your opponent.")
mood = input("How are you?\n")
print("Oh! I see that you're {}.".format(mood))
answer = input("Do you want to play a game? Answer Y for yes and N for no.\n")
if answer == "Y":
    print("Great! Let's play.")
elif answer == "N":
    print("Aww. Maybe another time.")
    quit()
else:
    print("You're silly. You should have answered Y or N. Try again.")
    quit()

name = input("Whats your name?\n")
print("Hello {}. Good luck!".format(name))

# Later, we'll figure out how to ask the user where they want to put their
# ships. For now, I'll just set them.
# coordinates:    0  1  2  3  4  5
computer_board = [0, 0, 1, 1, 0, 0]
human_board =    [1, 0, 0, 0, 0, 1]
computer_ships_left = sum(computer_board)
human_ships_left = sum(human_board)

# We'll use this to determine who gets to go
is_human_turn = True

# We'll use this to determine if the loop should keep going.
game_is_over = False

while not game_is_over:
    if is_human_turn:
        print("It's your turn!")

        coordinate = int(input("Where do you want to fire?"))
        print("You fired at {}".format(coordinate))
        if computer_board[coordinate] == 1:
            print("You hit!")
            # We update the board so that the fire is recorded
            computer_board[coordinate] = 0
            # since we hit they have one less ships
            computer_ships_left -= 1
        else:  # not board[coordinate] == 1
            print("You missed!")
        computer_ships_left = sum(computer_board)
        print("I have {} ships left. Keep going.".format(computer_ships_left))
    else:  # it's the computer's turn
        # For now the computer is silly and just fires at 0 always.
        # TODO: think about what strategy you use when picking squares.
        #       What might we program the computer to do? You don't have
        #       to write any code here.
        coordinate = 0
        print("I fired at {}".format(coordinate))
        if computer_board[coordinate] == 1:
            print("I hit!")
            human_board[coordinate] = 0
            human_ships_left -= 1
        else:  # not board[coordinate] == 1
            print("I missed!")
    # print now the player has moved, it'll be the other person's turn next.
    is_human_turn = not is_human_turn # so we just take the opposite!

    # Now it's your job again! Can you print the human's
    #          board and tell them how many ships they have left?
    # TODO: type your code to print the board

    # If we never update the game_is_over variable the condition
    # for our while loop will always be True and will loop over and
    # over and over and over and over and over... It's an infinite loop!
    # Can you try to update the game_is over_variable. You want
    # to use the number of ships left for each player and figure about
    # when one of them equals zero. You'll use those logical statements
    # we talked about before.
    # For example, I might have a program every morning that tells me
    # if I should take an umbrella that looks like this. I only
    # take an umbrella when it's already raining, the chance of rain is more
    # than 50, or it's the 13 of the month because I'm superstitious.\
    # rain_chance = 73
    # is_raining = False
    # day = 15
    # take_umbrella = is_raining or rain_chance >= 50 or day == 13
    # TODO: Use the computer_ships_left and human_ships_left to determine
    # if the game is over
    game_is_over = computer_ships_left == 0 or human_ships_left == 0

# We're outside the loop now. So someone won! Whoever has 0 ships left lost!
if human_ships_left == 0:
    print("I won! Thanks for the game! Better luck next time.")
elif computer_ships_left == 0:
    print("Wow! You're good! Great job winning!")
else:
    print("This shouldn't be possible if you wrote the game_is_over right.")
