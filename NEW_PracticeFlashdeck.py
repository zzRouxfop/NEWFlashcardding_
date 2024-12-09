from filefinder import *
from random import *
from CommaManagement import *

def practiceFlashdeck():
    printAllFlashdecks()
    title = str(input("which flashcard set would you like to open? [press ENTER to cancel]: "))
    if title == '':
        return None
    else:
        fTitle = 'flashdecks/' + title + ".txt"
        try:
            with open(fTitle, 'r') as f:
    
                Flashdeck = [l for l in f]
                shuffle(Flashdeck)
                
                CorrectGuesses = 0
                NumberOfQuestions = len(Flashdeck)
    
                for l in Flashdeck:
                    FlashdeckWithoutDisplayedFlashcard = [ll for ll in Flashdeck if ll != l]
                    FlashcardQuestion = khmerconverter(l)
                    print('\n')
                    print('• ' + FlashcardQuestion[0])
                    UserInput = str(input("press [ENTER] to reveal answer"))
    
                    print('• ' + FlashcardQuestion[1])
                    while True:
                        UserInput = str(input('did you get the answer right? [Y/N]: '))
                        UserInput.lower().strip()
    
                        if UserInput == 'y':
                            CorrectGuesses += 1
                            break
                        elif UserInput == 'n':
                            break
                        else:
                            print('invalid input!')
            
            print('\n')
            print(f'final score: {CorrectGuesses}/{NumberOfQuestions} | {int(CorrectGuesses / NumberOfQuestions * 100)}%')
    
        except FileNotFoundError:
            print(f"{title} not found!")


if __name__ == "__main__":
    practiceFlashdeck()
