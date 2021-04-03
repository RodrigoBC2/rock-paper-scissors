from random import randint

game_rules = {
    1: {
        'rock': ['paper'],
        'paper': ['scissors'],
        'scissors': ['rock']
    },
    2: {
        'rock': ['paper', 'spock'],
        'paper': ['scissors', 'lizard'],
        'scissors': ['rock', 'spock'],
        'lizard': ['rock', 'scissors'],
        'spock': ['lizard', 'paper']
    },
    # other rules if needed
}


def check_game_result(user_option, computer_option, winning_options):
    if user_option == computer_option:
        return 'draw'
    else:
        return 'user' if user_option in winning_options[computer_option] else 'computer'


def get_user_input(input_question, valid_options):
    user_input = ''
    while user_input not in valid_options:
        user_input = input(input_question + ' [' + (', '.join(valid_options)) + ']: ').lower()
    return user_input


game_type = int(get_user_input('Choose game type', ['1', '2']))

current_game_rules = game_rules[game_type]
current_game_rules_options = list(current_game_rules.keys())

user_choice = get_user_input('Type user choice', current_game_rules_options)
computer_choice = current_game_rules_options[randint(0, 2)]
result = check_game_result(user_choice, computer_choice, current_game_rules)

print('User:', user_choice)
print('Computer:', computer_choice)
print('Winner:', result)
