'''
    gridFunctions.py
    Valentin Pelloin - 14/10/2016
    MIT License
    Version 0.1

    ====

    Grid functions that calculate the game.

'''

def printGame(game):
    for i in game:
        print i

def addPiece(game, player, column):
    game[0][0] = 1
