from DungeonMaster import DMTools
from DungeonMaster import bcolors
from PlayerInputManager import InputManager

class Player:
    def characterCreation():
        print('Hello Adventurer, I hope you are ready.')
        print('Please, state your name. Something I can etch upon your epitaph.')

        playerName = input('State your name: ')
        playerName = bcolors.OKBLUE + playerName + bcolors.ENDC
        print('Ahh', playerName, 'there is something about you yes...')
        playerAge = input('How old did you say you were?: ')
        print('Still looking as good as ever', end="")
        DMTools.callPause(1)
        print('')
        print('')
        print('I\'m sorry, what race did you say you were?')
        ## iterate races here
        playerRace = InputManager.ParsePlayerInput(input(": "))
        print('')
        DMTools.SuspensePause(["Well", playerName, "have you made a name for yourself?"])
        DMTools.callPause(1)
