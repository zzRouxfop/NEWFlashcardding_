import os

def printAllFlashdecks(directory = 'flashdecks/'):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        print(filename[0:-4])
