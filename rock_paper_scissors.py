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

options_counter = {'user_counter': {'rock':[], 'paper': [], 'scissors': []},
                   'computer_counter': {'rock':[], 'paper': [], 'scissors': []} }

# function that extract information about the game results from the scoreboard dictionary
def game_statistics(game_scoreboard, user, rand):

    # sum the number os times player and computer wins and draws.
    player_wins = sum(game_scoreboard['player'])
    computer_wins = sum(game_scoreboard['computer'])
    match_draws = sum(game_scoreboard['draw'])

    # saving the option selected from user in a dictionary
    if user == 1:
        options_counter['user_counter']['rock'].append(1)
    elif user == 2:
        options_counter['user_counter']['paper'].append(1)
    else:
        options_counter['user_counter']['scissors'].append(1)

    if rand == 1:
        options_counter['computer_counter']['rock'].append(1)
    elif rand == 2:
        options_counter['computer_counter']['paper'].append(1)
    else:
        options_counter['computer_counter']['scissors'].append(1)

    sum_rock = sum([sum(options_counter['user_counter']['rock']), sum(options_counter['computer_counter']['rock'])])
    sum_paper = sum([sum(options_counter['user_counter']['paper']), sum(options_counter['computer_counter']['paper'])])
    sum_scissors = sum([sum(options_counter['user_counter']['scissors']), sum(options_counter['computer_counter']['scissors'])])

    return player_wins, computer_wins, match_draws, options_counter, sum_rock, sum_paper, sum_scissors

reboot = True

# loop to reload the game
while reboot == True:

    # dictionary populated with options
    opt_dict = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}

    print('Choose one of the options below:')
    print('Option 1 = ROCK.\nOption 2 = PAPER.\nOption 3 = SCISSORS.')

    # inputs from user
    user = int(input())

    # while loop added to make sure that user input is between 1 and 3
    while user != 1 and user != 2 and user != 3:
        print('Choose one of the options below:')
        print('Option 1 = ROCK.\nOption 2 = PAPER.\nOption 3 = SCISSORS.')
        user = int(input())

    # computer input (random)
    rand = randint(1, 3)

    # checking the choice of the players
    print("The user choice is: ", opt_dict.get(user))
    print("The computer choice is: ", opt_dict.get(rand))


    # variable that obtains the result given by "check_bet" function
    game_result = check_bet(user, rand)

    # use the game_score function to put the results in a dictionary
    game_scoreboard = game_score(game_result)

    # using the game statistics function
    player_wins, computer_wins, match_draws, options_counter, sum_rock, sum_paper, sum_scissors = game_statistics(game_scoreboard, user, rand)

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
        # printing rock, paper and scissors used by the player and computer
        print("The number of times player choose rock: ", sum(options_counter['user_counter']['rock']))
        print("The number of times player choose paper: ", sum(options_counter['user_counter']['paper']))
        print("The number of times player choose scissors: ", sum(options_counter['user_counter']['scissors']))

        print("The number of times computer choose rock: ", sum(options_counter['computer_counter']['rock']))
        print("The number of times computer choose paper: ", sum(options_counter['computer_counter']['paper']))
        print("The number of times computer choose scissors: ", sum(options_counter['computer_counter']['scissors']))

        print("Number of times Rock was chosen: ", sum_rock)
        print("Number of times Paper was chosen: ", sum_paper)
        print("Number of times Scissors was chosen: ", sum_scissors)

        reboot = False
