import random
from CommaManagement import *
from filefinder import *

def quizFlashdeck():
    printAllFlashdecks()
    title = str(input("which flashcard set would you like to open?: "))
    QuantityOfChoicesPerQuestion = int(input("how many choices per multiple choice? [3/4/5]: "))
    fTitle = 'flashdecks/' + title + ".txt"
    CorrectGuesses = 0
    try:
        with open(fTitle, 'r') as f:

            Flashdeck = [l for l in f]
            random.shuffle(Flashdeck)
            
            for l in Flashdeck:
                FlashdeckWithoutDisplayedFlashcard = [ll for ll in Flashdeck if ll != l]
                FlashcardQuestion = khmerconverter(l)
                print('\n')
                print('• ' + FlashcardQuestion[0])

                MultipleChoice = [FlashcardQuestion[1]]
                for x in range(QuantityOfChoicesPerQuestion - 1):
                    ChosenWrongAnswer = random.choice(FlashdeckWithoutDisplayedFlashcard)
                    FlashdeckWithoutDisplayedFlashcard.remove(ChosenWrongAnswer)
                    ChosenWrongAnswer = khmerconverter(ChosenWrongAnswer)
                    MultipleChoice.append(ChosenWrongAnswer[1])
                random.shuffle(MultipleChoice)

                counter = 1
                for l in MultipleChoice:
                    print(f"{counter}. {l}")
                    counter += 1
                
                counter = 1
                StringToPromptUserInput = 'answer ['
                for l in MultipleChoice:
                    StringToPromptUserInput += f'{str(counter)}/'
                    counter += 1
                StringToPromptUserInput = StringToPromptUserInput[0:-1]
                StringToPromptUserInput += ']: '

                while True:
                    UserInput = input(StringToPromptUserInput)
                    try:
                        UserInput = int(UserInput)
                        if 1 <= UserInput <= counter:
                            NumberOfQuestions = len(Flashdeck)
                            #line 10 should be here
                            UserInput -= 1
                            if MultipleChoice[UserInput] == FlashcardQuestion[1]:
                                CorrectGuesses += 1
                                break
                            else:
                                break
                        else:
                            print('invalid input!')
                    except:
                        print('invalid input!')
        print('\n')
        print(f'final score: {CorrectGuesses}/{NumberOfQuestions} | {int(CorrectGuesses / NumberOfQuestions * 100)}%')

    except FileNotFoundError:
        print(f'{title} not found!')

if __name__ == "__main__":
    quizFlashdeck()