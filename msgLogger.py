'''
    msgLogger.py
    Valentin Pelloin - 15/10/2016
    MIT License
    Version 0.1

    ====

    Terminal colors, using ANSI escape sequences and logging

'''
from time import gmtime, strftime

HEADER  = '\033[95m'
SUCCESS = '\033[36m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
RESET   = '\033[0m'
WHITE   = '\033[37m'



def logMsg(color, name, message):

    #Print message into the terminal
    print WHITE + "[" + color + name + WHITE + "] " + RESET + message

    #Save message to logs.log
    time = strftime("%d/%m/%y-%H:%M:%S", gmtime())
    text = ": [" + name + "] " + message + "\n"

    with open("logs.log", "a") as logFile:
        if color == WARNING:
            logFile.write(           time + " WARNING  " + text)
        elif color == FAIL:
            logFile.write(           time + " ERROR    " + text)
        elif color == HEADER:
            logFile.write("\n\n\n" + time + " STARTING " + text)
        else:
            logFile.write(           time + " INFO     " + text)
