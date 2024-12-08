from CommaManagement import *
import os 
import random
import string

def makeFlashdeck():
    
    while True:
        title = str(input("Flashdeck Name: "))
        if title == '':
            print('flashdeck title must NOT be blank!')
        else:
            break
        
    fTitle = 'flashdecks/' + title + '.txt'
    flashdeck = []

    with open(fTitle, 'w') as f:

        while True:
            question = str(input(f"question (type in [X] to close flashdeck): "))
            question.strip()
            if question == 'x' or question == 'X':
                if len(flashdeck) < 5:
                    print('you must have at least 5 flashcards in your flashdeck!')
                break

            answer = str(input('answer: '))
            answer.strip()
            flashdeck.append(commaconverter((question, answer)))
            print(f"flashcard \'{question}\' addded!")
        
        for l in flashdeck:
            f.write(','.join(l) + ',\n')

        print(f'{title} added!')


if __name__ == "__main__":
    makeFlashdeck()