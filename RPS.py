import random

def rps_play() :
    print("You're challenged to a Rock Paper Scissors Match!")
    player = input("Type r for Rock, p for Paper, and s for Scissors!\n" )
    enemy = random.choice(['r', 'p', 's'])

    if player == enemy:
        return 'tie'

    if win_con(player, enemy):
        print("Congratulations! Player has won the match!")
        play_again()

    else:
        print("Player has lost!")
        play_again()

def win_con(player, enemy):
    if(player == 'r' and enemy == 's' ) or (player == 's' and enemy == 'p')  \
    or ( player == 'p' and enemy == 'r'):
        return True

def play_again():
    play_another = input("Play another game? Type Y/n!\n")
    if play_another == 'Y' or play_another == 'y':
        rps_play()

    quit()

rps_play()