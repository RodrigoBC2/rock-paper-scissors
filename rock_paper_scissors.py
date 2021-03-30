# library to generate "random" numbers
from random import randint

# dictionary populated with all options, including the extended version
opt_dict = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS', 4: 'LIZARD', 5: 'SPOCK'}

# dictionary that use values as user input and a list that corresponding with loser options from the opponent
options_bigbang = {1: ['PAPER', 'LIZARD'],
                   2: ['ROCK', 'SPOCK'],
                   3: ['SCISSORS', 'LIZARD'],
                   4: ['PAPER', 'SPOCK'],
                   5: ['SCISSORS', 'ROCK']}


# function to check multiple choices
def big_bang_bet(user, rand):
    # checking if the options name are equals
    if opt_dict.get(rand) == opt_dict.get(user):

        return 'A Draw!'

    # checking if the computer option name is included in the list of the player's choice. If so, user wins.
    elif opt_dict.get(rand) in options_bigbang.get(user):

        return 'User has won!'

    # if the computer option name is not on the list, it means the computer wins.
    else:

        return 'Computer has won!'


# dictionary to buffer the options selected by user
options_user_counter = {'rock': 0,
                        'paper': 0,
                        'scissors': 0,
                        'lizard': 0,
                        'spock': 0}
# dictionary to buffer the options selected by computer
options_computer_counter = {'rock': 0,
                            'paper': 0,
                            'scissors': 0,
                            'lizard': 0,
                            'spock': 0}

# dictionary created to sum the options selected from both competitors
options_total_sum = {'rock': 0,
                     'paper': 0,
                     'scissors': 0,
                     'lizard': 0,
                     'spock': 0}


# function created to counter the full extended game statistics
def big_bang_statistics(user, rand):
    # incrementing user selected options in a dictionary
    if user == 1:
        options_user_counter['rock'] += 1
    elif user == 2:
        options_user_counter['paper'] += 1
    elif user == 3:
        options_user_counter['scissors'] += 1
    elif user == 4:
        options_user_counter['lizard'] += 1
    else:
        options_user_counter['spock'] += 1

    # incrementing computer selected options in a dictionary
    if rand == 1:
        options_computer_counter['rock'] += 1
    elif rand == 2:
        options_computer_counter['paper'] += 1
    elif rand == 3:
        options_computer_counter['scissors'] += 1
    elif rand == 4:
        options_computer_counter['lizard'] += 1
    else:
        options_computer_counter['spock'] += 1

    # retrieving all sums and returning them to display the total amount of options that has been chosen.
    options_total_sum['rock'] = options_user_counter['rock'] + options_computer_counter['rock']
    options_total_sum['paper'] = options_user_counter['paper'] + options_computer_counter['paper']
    options_total_sum['scissors'] = options_user_counter['scissors'] + options_computer_counter['scissors']
    options_total_sum['lizard'] = options_user_counter['lizard'] + options_computer_counter['lizard']
    options_total_sum['spock'] = options_user_counter['spock'] + options_computer_counter['spock']

    return options_user_counter, options_computer_counter, options_total_sum


# dictionary that uses values as player's choice and keys as the option that loses for the player's option.
options_default = {1: 'SCISSORS',
                   2: 'ROCK',
                   3: 'PAPER'}


# function to check if computer's choice is the same option that loses for the player's option
def check_bet(user, rand):
    # verifying if the game is a draw
    if opt_dict.get(user) == opt_dict.get(rand):

        return 'A Draw!'

    # checking if the computer option name is the same string in the player's choice. If so, user wins.
    elif opt_dict.get(rand) in options_default.get(user):

        return 'User has won!'

    # if not the same, that means the computer won.
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
                    'computer_streak': 0}


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


# function that extract information about the game results from the scoreboard dictionary
def game_default_statistics(user, rand):
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

    options_total_sum['rock'] = options_user_counter['rock'] + options_computer_counter['rock']
    options_total_sum['paper'] = options_user_counter['paper'] + options_computer_counter['paper']
    options_total_sum['scissors'] = options_user_counter['scissors'] + options_computer_counter['scissors']

    return options_user_counter, options_computer_counter, options_total_sum


# explaining both types of the game: Default and extended version
print('There are 2 types of the game "rock, paper and scissors": The usual game with 3 choices as mentioned before '
      'and the expansion created by Sam Kass with Karen Bryla: Rock, Paper, Scissors, Lizard, Spock')

print('\nPress "1" to select the original game or press "2" to play the expansion')

game_choice = int(input())

while game_choice != 1 and game_choice != 2:
    print('Please, enter "1" to select the original game or "2" to play the expansion')
    game_choice = int(input())

# if the player choose the default version, then the code only uses the functions related to the default game.
if game_choice == 1:

    reboot_bigbang = True

    while reboot_bigbang:

        print('Choose one of the options below:')
        print('Enter "1" for ROCK.\nEnter "2" for PAPER.\nEnter "3" for SCISSORS.')

        # inputs from user
        user = int(input())

        # computer input (random)
        rand = randint(1, 3)

        # checking the choice of the players
        print("The user choice is: ", opt_dict.get(user))
        print("The computer choice is: ", opt_dict.get(rand))

        # variable that obtains the result given by "check_bet" function
        game_result = check_bet(user, rand)

        # use the game_score function to put the results in a dictionary
        game_score(game_result)

        game_default_statistics(user, rand)

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
            print("The number of times player choose rock: ", options_user_counter['rock'])
            print("The number of times player choose paper: ", options_user_counter['paper'])
            print("The number of times player choose scissors: ", options_user_counter['scissors'])

            print("The number of times computer choose rock: ", options_computer_counter['rock'])
            print("The number of times computer choose paper: ", options_computer_counter['paper'])
            print("The number of times computer choose scissors: ", options_computer_counter['scissors'])

            # printing the number of times each item was chosen
            print("Number of times Rock was chosen: ", options_total_sum['rock'])
            print("Number of times Paper was chosen: ", options_total_sum['paper'])
            print("Number of times Scissors was chosen: ", options_total_sum['scissors'])

            # print the win streak of each player
            print("Player wins in a roll: ", win_streak_score['player_streak'])
            print("Computer wins in a roll: ", win_streak_score['computer_streak'])

            reboot_bigbang = False

else:
    reboot = True

    # loop to reload the game
    while reboot:

        print('Choose one of the options below:')
        print('Option 1 = ROCK.\nOption 2 = PAPER.\nOption 3 = SCISSORS. \nOption 4 = LIZARD. \nOption 5 = SPOCK')

        # inputs from user
        user = int(input())

        # computer input (random)
        rand = randint(1, 5)

        print("The user choice is: ", opt_dict.get(user))
        print("The computer choice is: ", opt_dict.get(rand))

        game_result = big_bang_bet(user, rand)

        # use the game_score function to put the results in a dictionary
        game_score(game_result)
        big_bang_statistics(user, rand)

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
            # printing rock, paper, scissors, lizard and spock used by the player and computer
            print("The number of times player choose rock: ", options_user_counter['rock'])
            print("The number of times player choose paper: ", options_user_counter['paper'])
            print("The number of times player choose scissors: ", options_user_counter['scissors'])
            print("The number of times player choose lizard: ", options_user_counter['lizard'])
            print("The number of times player choose spock: ", options_user_counter['spock'])

            print("The number of times computer choose rock: ", options_computer_counter['rock'])
            print("The number of times computer choose paper: ", options_computer_counter['paper'])
            print("The number of times computer choose scissors: ", options_computer_counter['scissors'])
            print("The number of times computer choose lizard: ", options_computer_counter['paper'])
            print("The number of times computer choose spock: ", options_computer_counter['spock'])

            # printing the number of times each item was chosen
            print("Number of times Rock was chosen: ", options_total_sum['rock'])
            print("Number of times Paper was chosen: ", options_total_sum['paper'])
            print("Number of times Scissors was chosen: ", options_total_sum['scissors'])
            print("Number of times Lizard was chosen: ", options_total_sum['lizard'])
            print("Number of times Sock was chosen: ", options_total_sum['spock'])

            # print the win streak of each player
            print("Player wins in a roll: ", win_streak_score['player_streak'])
            print("Computer wins in a roll: ", win_streak_score['computer_streak'])

            reboot = False
