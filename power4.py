'''
    power4.py
    Valentin Pelloin - 14/10/2016
    MIT License
    Version 0.1

    ====

    This is the main file for the twitter bot power4

'''

# -------
# Imports
import tweepy
import sys
import os

# Import config file
from config import *
from msgLogger import *
from gridFunctions import *


# ---------
# Init game

game = [[0 for x in range(N_COLUMN)] for x in range(N_LINE)]


# Clear terminal and print log
os.system('clear')
logMsg(HEADER, "power4", "Loading power4 bot ...\n")



# ---------------
# Auth to twitter
auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
auth.set_access_token(Access_Key, Access_Secret)

try:
    redirect_url = auth.get_authorization_url()
    logMsg(SUCCESS, "Twitter", "Successfully logged in Twitter.")
except tweepy.TweepError:
    logMsg(FAIL, "Twitter", "Error! Wrong tokens. Check your config.py (or configSAMPLE.py if not present).")
    sys.exit()

api = tweepy.API(auth)

column = 2
line = addPiece(game, PLAYER_1, column)
if line == -1:
    print "error"
else:
    print "Piece added in : ["+ str(line) + "]["+str(column)+"]"
    printGame(game)



logMsg(WARNING, "power4", "End of power4.py, quitting.")
#api.update_status('Yeah, that rocks!')
