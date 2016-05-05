from DungeonMaster import DMTools
from DungeonMaster import bcolors
from PlayerInputManager import InputManager

class Player:

    def characterCreation():

        global playerRace
        global playerName
        global playableRaces

        playableRaces = ["Human", "Dwarf", "Elf", "Halfling", "Dragonborn", "Gnome", "Half-Orc"]


        print('Hello Adventurer, I hope you are ready.')
        print('Please, state your name. Something I can etch upon your epitaph.')

        Player.playerName = input('State your name: ')
        Player.playerName = bcolors.OKBLUE + Player.playerName + bcolors.ENDC
        print('Ahh', Player.playerName, 'there is something about you yes...\n\n')
        print('I\'m sorry, what race did you say you were?')
        for races in playableRaces:
            print('     -->', races)
        print('')
        print('! To assign race, type\'/setRace <RACE>\' !')
        while InputManager.correctCommand != True:
            Player.playerRace = InputManager.ParsePlayerInput(input(": "))
        print('')
        DMTools.SuspensePause(["Well", playerName, "have you made a name for yourself?"])
        DMTools.callPause(1)
