import os
from CharacterSheet import Player
from sys import platform as _platform

def initGameConf():
    ## Let's clear the screen to start.
    if _platform == "linux" or _platform == "linux2":
        os.system('clear')
        # linux
    elif _platform == "darwin":
        os.system('clear')
        # OS X
    elif _platform == "win32":
        os.system('cls')
        # Windows...

    Player.characterCreation()

initGameConf()
