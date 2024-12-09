from filefinder import *
from NEW_MakeFlashdeck import *
from NEW_QuizFlashdeck import *
from NEW_EditFlashdeck import *
from NEW_PracticeFlashdeck import *
from NEW_GetFlashcardFromFlashdeck import *
from DelFlashcard import *

def MainMenu():
    while True:
        print('- - - - - - - - - - \ntype [L] to get flashdecks\ntype [M] to make flashdeck\ntype [P] to get flashcards of a flashdeck\n- - - - - - - - - - \ntype [F] to practice a flashdeck\ntype [Q] to quiz yourself on a flashdeck\n- - - - - - - - - -\ntype [E] to edit an existing flashdeck\ntype [D] to delete a flashdeck\ntype [X] to exit\n- - - - - - - - - - \n')
        inputting = str(input(">>> "))

        inputting = inputting.strip().lower()

        if inputting == 'm':
            makeFlashdeck()
        elif inputting == 'l':
            print('your Flashdecks:')
            printAllFlashdecks()
        elif inputting == 'q':
            quizFlashdeck()
        elif inputting == 'f':
            practiceFlashdeck()
        elif inputting == 'e':
            EditFlashdeck()
        elif inputting == 'd':
            DelFlashcard()
        elif inputting == 'p':
            GetFlashcardFromFlashdeck()
        elif inputting == 'x':
            exit()
        else:
            print('invalid input!')
