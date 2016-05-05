from DungeonMaster import bcolors
from random import randint

class InputManager:

    correctCommand = False

    def ParsePlayerInput(playerInput):

        commandTokens = ["/yell", "/roll", "/say", "/grab", "/pickup", "/setRace"]
        ## by character
        playerInputTokens = list(playerInput)
        ## by string
        splitPlayerInput = playerInput.split()

        if splitPlayerInput[0] in commandTokens:
            InputManager.correctCommand = True
            ## LETS ROLL SOME DICE!
            if '/roll' in splitPlayerInput:
                if 'd20' in splitPlayerInput[1]:
                    analyzeRollParse = list(splitPlayerInput[1])
                    if analyzeRollParse[0] != 'd':
                        for rollTime in range(0, int(analyzeRollParse[0])):
                            print(bcolors.OKGREEN + "You rolled: ", randint(0, 20), "" + bcolors.ENDC)
                    else:
                        print(bcolors.OKGREEN + "You rolled: ", randint(0, 20), "" + bcolors.ENDC)
                if 'd12' in splitPlayerInput[1]:
                    analyzeRollParse = list(splitPlayerInput[1])
                    if analyzeRollParse[0] != 'd':
                        for rollTime in range(0, int(analyzeRollParse[0])):
                            print(bcolors.OKGREEN + "You rolled: ", randint(0, 12), "" + bcolors.ENDC)
                    else:
                        print(bcolors.OKGREEN + "You rolled: ", randint(0, 12), "" + bcolors.ENDC)
                if 'd10' in splitPlayerInput[1]:
                    analyzeRollParse = list(splitPlayerInput[1])
                    if analyzeRollParse[0] != 'd':
                        for rollTime in range(0, int(analyzeRollParse[0])):
                            print(bcolors.OKGREEN + "You rolled: ", randint(0, 10), "" + bcolors.ENDC)
                    else:
                        print(bcolors.OKGREEN + "You rolled: ", randint(0, 10), "" + bcolors.ENDC)

            if '/setRace' in splitPlayerInput:
                from CharacterSheet import Player
                if splitPlayerInput[1] in Player.playableRaces:
                    Player.playerRace == splitPlayerInput[1]
                    print(Player.playerRace)

        ## Now if no command meets the anything in the list of commands.
        else:
            print(bcolors.FAIL + "Please enter a valid command." + bcolors.ENDC)
