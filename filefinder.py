import os

def printAllFlashdecks(directory = 'flashdecks/'):
    if directory not in os.listdir():
        makeDir = input(f"there is no flashdecks directory called '{directory}'. Make one? [Y/n]")
        if makeDir.lower() == 'y':
            os.mkdir('flashdecks')
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        print(filename[0:-4])
