# library to generate "random" numbers
from random import randint


# library to substitute all if and elif from the first version of the code
def check_bet(user, rand):
    # verifying if the game is a draw
    if user == rand:
        winner = 'A Draw!'
        return winner

    # shrink all user possibilities to win in a single condition
    elif user == 1 and rand != 2 or user == 2 and rand != 3 or user == 3 and rand != 1:

        winner = 'User has won!'
        return winner

    # if none of conditions above is satisfied, then the computer wins
    else:

        winner = 'Computer has won!'
        return winner


# scoreboard dictionary to store game results
scoreboard = {'draw': [],
              'player': [],
              'computer': []}


# function that returns a dictionary with winners information to make result analysis
def game_score(game_result):
    if game_result == 'A Draw!':
        scoreboard['draw'].append(1)
        scoreboard['player'].append(0)
        scoreboard['computer'].append(0)

    elif game_result == 'User has won!':
        scoreboard['draw'].append(0)
        scoreboard['player'].append(1)
        scoreboard['computer'].append(0)

    else:
        scoreboard['draw'].append(0)
        scoreboard['player'].append(0)
        scoreboard['computer'].append(1)

    return scoreboard


# function that extract information about the game results from the scoreboard dictionary
def game_statistics(game_scoreboard):
    player_wins = sum(game_scoreboard['player'])
    computer_wins = sum(game_scoreboard['computer'])
    match_draws = sum(game_scoreboard['draw'])

    return player_wins, computer_wins, match_draws


reboot = True

# loop to reload the game
while reboot == True:

    # dictionary populated with options
    opt_dict = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}

    print('Choose one of the options below:')
    print('Option 1 = ROCK.\nOption 2 = PAPER.\nOption 3 = SCISSORS.')

    # inputs from user and computer
    user = int(input())
    rand = randint(1, 3)

    # checking the choice of the players
    print("The user choice is: ", opt_dict.get(user))
    print("The computer choice is: ", opt_dict.get(rand))

    # variable that obtains the result given by "check_bet" function
    game_result = check_bet(user, rand)

    # use the game_score function to put the results in a dictionary
    game_scoreboard = game_score(game_result)

    # using the game statistics function
    player_wins, computer_wins, match_draws = game_statistics(game_scoreboard)

    # printing the result on screen
    print("The result is: ", game_result)

    # printing game statistics on screen
    print("Player score: ", player_wins)
    print("Computer score: ", computer_wins)
    print("Draws score: ", match_draws)

    # user input choosing play again, "yes" and "not" notation.
    choice = input("\nDo you want to play again? press y if yes or n if not\n")

    # loop created to avoid any other input than yes or not keys
    while choice != 'y' and choice != 'n':
        choice = input("\nDo you want to play again? press y if yes or n if not\n")

    # if yes, the initial loop still active
    if choice == 'y':
        reboot = True

    # if not, the initial variable will kill the while loop, finishing the program.
    else:
        reboot = False
