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


def check_result(user_choice, computer_choice, game_type):
    if user_choice == computer_choice:
        return 'draw'
    else:
        return 'user' if user_choice in game_rules[game_type][computer_choice] else 'computer'


def get_user_choice(game_type):
    valid_options = game_rules[game_type].keys()
    user_choice = ''
    while user_choice not in valid_options:
        user_choice = input("Choose " + (', '.join(valid_options)) + ": ").lower()
    return user_choice


game_type = int(input("Select game type (1 or 2): "))
user_choice = get_user_choice(game_type)
computer_choice = list(game_rules[game_type].keys())[randint(0, 2)]

print("User:", user_choice)
print("Computer:", computer_choice)

result = check_result(user_choice, computer_choice, game_type)
print("Winner:", result)
