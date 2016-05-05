from DungeonMaster import bcolors
from random import randint

class InputManager:
    def ParsePlayerInput(playerInput):
        commandTokens = ["/yell", "/roll", "/say", "/grab", "/pickup"]
        ## by character
        playerInputTokens = list(playerInput)
        ## by string
        splitPlayerInput = playerInput.split()

        if splitPlayerInput[0] in commandTokens:
            ## LETS ROLL SOME DICE!
            if '/roll' in splitPlayerInput:
                if 'd20' in splitPlayerInput[1]:
                    analyzeRollParse = list(splitPlayerInput[1])
                    if analyzeRollParse[0] != 'd':
                        for rollTime in range(0, int(analyzeRollParse[0])):
                            print(bcolors.OKGREEN + "You rolled: ", randint(0, 20), "" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "Please enter a valid command." + bcolors.ENDC)
