# library to generate "random" numbers
from random import randint


# library to substitute all if and elif from the first version of the code
def check_bet(user, rand):

    # verifying if the game is a draw
    if user == rand:
        return 'A Draw!'

    # shrink all user possibilities to win in a single condition
    elif user == 1 and rand != 2 or user == 2 and rand != 3 or user == 3 and rand != 1:
        return 'User has won!'

    # if none of conditions above is satisfied, then the computer wins
    else:
        return 'Computer has won!'

# scoreboard dictionary to store game results
scoreboard = {'draw': 0,
              'player': 0,
              'computer': 0}

# win_streak dictionary created as a buffer, returning the maximum amount of wins in a roll each player scored.
win_streak = {'win_player': 0,
              'win_computer': 0}

# win_streak_score dictionary was created to save the highest win streak of each player.
win_streak_score = {'player_streak': 0,
                    'computer_streak':0}

# function that returns a dictionary with winners information to make result analysis
def game_score(game_result):

    # this conditional sets a threshold to start streak count and save the last and bigger streak score.
    if win_streak['win_player'] > 2 and win_streak['win_player'] >= win_streak_score['player_streak']:
        win_streak_score['player_streak'] = win_streak['win_player']

    # elif instead of else due to necessary conditions to make the streak count.
    elif win_streak['win_computer'] > 1 and win_streak['win_computer'] >= win_streak_score['computer_streak']:
        win_streak_score['computer_streak'] = win_streak['win_computer']

    # if it is a draw, the partial streak count is set to zero.
    if game_result == 'A Draw!':
        scoreboard['draw'] += 1
        win_streak['win_player'] = 0
        win_streak['win_computer'] = 0

    # if player wins, streak score start counting and win score is updated
    elif game_result == 'User has won!':
        scoreboard['player'] += 1
        win_streak['win_player'] += 1
        win_streak['win_computer'] = 0

    # if computer wins, streak score start counting and win score is updated
    else:
        scoreboard['computer'] += 1
        win_streak['win_player'] = 0
        win_streak['win_computer'] += 1


    return scoreboard, win_streak_score

# dictionary to buffer the options selected by user
options_user_counter = {'rock': 0,
                        'paper': 0,
                        'scissors': 0}
# dictionary to buffer the options selected by computer
options_computer_counter = {'rock': 0,
                            'paper': 0,
                            'scissors': 0}

# function that extract information about the game results from the scoreboard dictionary
def game_statistics(user, rand):

    # incrementing user selected options in a dictionary
    if user == 1:
        options_user_counter['rock'] += 1
    elif user == 2:
        options_user_counter['paper'] += 1
    else:
        options_user_counter['scissors'] += 1

    # incrementing computer selected options in a dictionary
    if rand == 1:
        options_computer_counter['rock'] += 1
    elif rand == 2:
        options_computer_counter['paper'] += 1
    else:
        options_computer_counter['scissors'] += 1

    # sum every option to give the number of times each option was selected from both competitors
    sum_rock = sum(options_user_counter['rock'], options_computer_counter['rock'])
    sum_rock = sum(options_user_counter['rock'], options_computer_counter['rock'])
    sum_rock = sum(options_user_counter['rock'], options_computer_counter['rock'])

    return sum_rock, sum_paper, sum_scissors

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

    # call game_statistics function to show information about rock, paper ans scissors count and selections
    sum_rock, sum_paper, sum_scissors = game_statistics(user, rand)

    # printing the result on screen
    print("The result is: ", game_result)

    # printing game statistics on screen
    print("Player score: ", scoreboard['player'])
    print("Computer score: ", scoreboard['computer'])
    print("Draws score: ", scoreboard['draw'])

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

        # printing the number of times each item was chosen
        print("Number of times Rock was chosen: ", sum_rock)
        print("Number of times Paper was chosen: ", sum_paper)
        print("Number of times Scissors was chosen: ", sum_scissors)

        # print the win streak of each player
        print("Player wins in a roll: ", win_streak_score['player_streak'])
        print("Computer wins in a roll: ", win_streak_score['computer_streak'])

        reboot = False
