import os
import time

def printAllFlashdecks(directory = 'flashdecks'):
    if directory not in os.listdir():
        makeDir = input(f"there is no flashdecks directory called '{directory}'. One will be made shortly...")
        time.sleep(5)
        os.mkdir('flashdecks')
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        print(filename[0:-4])
