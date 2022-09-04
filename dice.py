import pandas as pd
import numpy as np
import os
import random


def dice_roll():
    return random.randint(1, 6)


def play_game():
    player_1 = dice_roll()
    player_2 = dice_roll()


    print("Player 1 got: {} and Player 2 got: {}".format(player_1, player_2))

    if player_1 == player_2:
        print("It's a Draw!!")
    elif player_1 > player_2:
        print("Player 1 wins this round!")
        print("Player 1 is thirsty for more matches!")
        print("Player 1 drinks soda!")
    else:
        print("Player 2 wins this round!")
        print("Player 2 is thirsty for more matches!")
        print("Player 2 drinks soda!")

play_game()
