from CommaManagement import *
from filefinder import *
import random
import string

def EditFlashdeck():
    printAllFlashdecks()
    title = str(input("which flashcard set would you like to edit?: "))
    fTitle = 'flashdecks/' + title + ".txt"
    try:
        with open(fTitle, 'r') as f:

            Flashdeck = [l for l in f]
            RevisedFlashdeck = []

            for l in Flashdeck:
                FlashcardToEdit = khmerconverter(l)
                print(f"\nquestion: {FlashcardToEdit[0]}\nanswer: {FlashcardToEdit[1]}\n")
                while True:
                    UserInputToEditFlashcard = str(input("press [Q] to edit the question\npress [A] to edit the answer\npress [B] to edit both question and answer\npress [R] to remove flashcard\npress [C] to continue to next flashcard\n>>>"))
                    # press [Q] to edit the question
                    # press [A] to edit the answer
                    # press [B] to edit both question and answer
                    # press [R] to remove flashcard
                    # press [C] to continue to next flashcard

                    UserInputToEditFlashcard.lower().strip()
                    if UserInputToEditFlashcard == 'r':

                        break

                    elif UserInputToEditFlashcard == 'c':
                        RevisedFlashdeck.append(l)
                        break

                    elif UserInputToEditFlashcard == 'q':
                        NewQuestion = str(input("new question: "))
                        FlashcardToEdit[0] = NewQuestion
                        FlashcardToEdit = ','.join(commaconverter(FlashcardToEdit))
                        RevisedFlashdeck.append(FlashcardToEdit + ',\n')
                        break

                    elif UserInputToEditFlashcard == 'a':
                        NewAnswer = str(input('new answer: '))
                        FlashcardToEdit[1] = NewAnswer
                        FlashcardToEdit = ','.join(commaconverter(FlashcardToEdit))
                        RevisedFlashdeck.append(FlashcardToEdit + ',\n')
                        break
                        
                    elif UserInputToEditFlashcard == 'b':
                        NewQuestion = str(input("new question: "))
                        NewAnswer = str(input('new answer: '))
                        RevisedFlashdeck.append(','.join(commaconverter([NewQuestion, NewAnswer])) + ',\n')
                        break
                    else:
                        print('invalid input!')
        while True:
            UserInputToAddMoreFlashcardsToFlashdeck = str(input("would you like to add more flashcards to this flashdeck? [Y/N]: "))
            UserInputToAddMoreFlashcardsToFlashdeck.lower().strip()

            if UserInputToAddMoreFlashcardsToFlashdeck == 'n':
                print('done!')
                break
            elif UserInputToAddMoreFlashcardsToFlashdeck == 'y':
                while True:
                    question = str(input(f"question (type in [X] to close flashdeck): "))
                    question.strip()
                    if question == 'x' or question == 'X':
                        break

                    answer = str(input('answer: '))
                    answer.strip()
                    Flashdeck.append(','.join(commaconverter((question, answer))) + ',\n')
                    print(f"flashcard \'{question}\' addded!")
                break
            else:
                print('invalid input!')

        with open(fTitle, 'w') as f:
            for l in RevisedFlashdeck:
                f.write(l)
        print('done!')

    except FileNotFoundError:
        print(f'{title} not found!')

if __name__ == "__main__":
    EditFlashdeck()