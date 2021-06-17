import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

path = askdirectory(title='Which folder do you think it was in')  
Found_Places = []


fileToBeFound = input("What file are you looking for?   ")

for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        if file == fileToBeFound:
            Found_Places.append(f"Found this file in {dirpath}")
            print(f"Checking this {file} in",dirpath)
        else:
            print(f"Checking this {file} in",dirpath)

for place in Found_Places:
    print(place)