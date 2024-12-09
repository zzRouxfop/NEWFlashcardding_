import os
from filefinder import *

#deleting flashcards nothing much

def DelFlashcard():
    printAllFlashdecks()
    inputting = str(input('which flashdeck would you like to delete?[press ENTER to exit]: '))
    if inputting == '':
        return None
    f = 'flashdecks/' + inputting + '.txt'
    while True:
        warnUser = str(input('are you sure? this action can\'t be undone! [Y/N]: '))

        if warnUser == 'n':
            return None
        elif warnUser == 'y':
            print(f"{inputting} deleted! ")
            os.remove(f)
            return None
        else:
            print('invalid input!')