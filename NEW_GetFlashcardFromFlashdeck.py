from filefinder import *
from CommaManagement import *

def GetFlashcardFromFlashdeck():
    printAllFlashdecks()
    Title = str(input("which flashdeck would you like to view the flashcards from? [press ENTER to cancel]: "))
    if Title == '':
        pass
    else:
        fTitle = 'flashdecks/' + Title + '.txt'
        try:
            with open(fTitle, 'r') as f:
                Flashdeck = []
                for l in f:
                    Flashdeck.append(khmerconverter(l))
    
                counter = 1
                for l in Flashdeck:
                    print(f'\n{counter}:\n{l[0]}\n{l[1]}')
                    counter += 1
                print('\n')
    
        except FileNotFoundError:
            print(f'{Title} not found!')
