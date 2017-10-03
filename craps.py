# Kevin Chen
# 02/10/17
# This program is call craps and help people to count win rate of this game.

import random


def roll_dice():
    """
    This function represent the value of dices
    :return: random number between 2 to 12
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return total


def loop(how_many_times):
    """
    This function represent the win or lose of this craps game
    :param how_many_times: input by user,represent how many times the games are play
    :return: how many times it wins
    """
    win = 0
    lose = 0
    for x in range(how_many_times):

        total = roll_dice()

        if total == 7 or total == 11:
            win = win+1
        elif total == 2 or total == 3 or total == 12:
            lose = lose+1
        else:
            point = total
            while True:
                if roll_dice() == 7:
                    lose = lose+1
                    break
                elif roll_dice() == point:
                    win = win+1
                    break
    return win


def main():
    game = int(input("how many game would you like to simulate"))
    wins = loop(game)
    lose = game - wins
    print("you play", game, "games", "you win", wins, "you lose", lose)
    rate = wins/game
    print("your won", rate, "percent of the time")

main()
