import time
import sys
class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

class DMTools:
    def SuspensePause(message):
        for x in message:
            time.sleep(1.5)
            sys.stdout.write(x)
            sys.stdout.write(" ")
            sys.stdout.flush()

    def callPause(pauseDuration):
        for ellipsis in range(0, 3):
            time.sleep(pauseDuration)
            sys.stdout.write(".")
            sys.stdout.write(" ")
            sys.stdout.flush()
