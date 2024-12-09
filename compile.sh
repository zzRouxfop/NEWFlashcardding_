#!/bin/bash

pip install pyinstaller
pyinstaller --onefile --distpath ./ --icon="logo.ico" --name 'Flashdeck!' 'MAIN.py'
pip uninstall pyinstaller

rm MAIN.py
rm NEW_EditFlashdeck.py
rm NEW_Interface.py
rm NEW_MakeFlashdeck.py
rm NEW_PracticeFlashdeck.py
rm NEW_QuizFlashdeck.py
rm logo.ico
rm filefinder.py
rm DelFlashcard.py
rm CommaManagement.py NEW_GetFlashcardFromFlashdeck.py Flashdeck!.spec README.md LICENSE
rm -r build
rm compile.sh