import os
import sys

def readWatchList():
    """ Reads text file for watch list data. """
    pass 

def createConfigFolder():
    """ Creates directory for storing config data. """
    configDir = os.path.join(os.getcwd(), 'config')
    if not os.path.exists(configDir):
        os.mkdir(configDir)

def createWatchList():
    """ Creates file for storing watch list data. """
    pass