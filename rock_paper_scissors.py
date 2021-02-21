#library that generates random numbers
from random import randint

reboot = True

#loop to reload the game
while reboot == True:
    
    # dictionary populated with options
    opt_dict = {1 : 'ROCK', 2 : 'PAPER', 3 : 'SCISSORS'}
    
    print('Choose one of the options below:')
    print('Option 1 = ROCK.\nOption 2 = PAPER.\nOption 3 = SCISSORS.')
    
    user = int(input())
    
    # generating an integer random number and saving it in a variable
    rand = randint(1,3)

    pc = opt_dict.get(rand)
    
    # checking if the duel is a draw.
    if opt_dict.get(user) == pc:
        print('\n It is a DRAW!')
        
    # if its not a DRAW, than the program will check other options
    elif user == 1:
        print('User choose: ROCK.')
        print('Computer choose: ', pc)
        
        if pc == opt_dict.get(2):
            print('\nComputer has won!')
        
        elif pc == opt_dict.get(3):
            print('\nUser has won!')
    
    elif user == 2:
        print('User choose: PAPER.')
        print('Computer choose: ', pc)
        
        if pc == opt_dict.get(3):
            print('\nComputer has won!')
        
        elif pc == opt_dict.get(1):
            print('\nUser has won!')
        
    elif user == 3:
        print('User choose: SCISSORS.')
        print('Computer choose: ', pc)
        
        if pc == opt_dict.get(1):
            print('\nComputer has won!')
        
        elif pc == opt_dict.get(2):
            print('\nUser has won!')
    
    # user input choosing play again, "yes" and "not" notation.
    choice = input("\nDo you want to play again? press y if yes or n if not")
    
    # loop created to avoid any other input than yes or not keys
    while choice != 'y' and choice != 'n':
        
        choice = input("\nDo you want to play again? press y if yes or n if not\n")
    
    # if yes, the initial loop still active    
    if choice == 'y':
        reboot = True

    # if not, the initial variable will kill the while loop, finishing the program.    
    elif choice == 'n':
        reboot = False
