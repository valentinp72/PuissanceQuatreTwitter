'''
    gridFunctions.py
    Valentin Pelloin - 14/10/2016
    MIT License
    Version 0.1

    ====

    Grid functions that calculate the game.

'''


N_COLUMN = 7
N_LINE   = 5

PLAYER_1 = 1
PLAYER_2 = 2


# Add a piece to the specified column.
# Return -1 if there was an error about the column.
# Else, return the line where the piece was put
def addPiece(game, player, column):

    # If player is not PLAYER_1 or PLAYER_2
    if player != PLAYER_1 and player != PLAYER_2:
        return -1

    # If we can't put the piece into the column
    if column < 0 or column >= N_COLUMN or game[0][column] != 0:
        return -1

    i = N_LINE-1
    while game[i][column] != 0:
        i -= 1

    game[i][column] = player

    return i


def checkVert(game, lastPiece):
    print "yeah"
