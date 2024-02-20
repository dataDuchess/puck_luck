# Utility script to unzip and organize game-level hockey stats files from Kaggle
from zipfile import ZipFile

# Define variables
DATA_FOLDER = '../data/raw/'
FILE_NAME = 'NHL_game-Level.zip'
OUTPUT_FOLDER = '../data/interim/'

# Unzip archive folder
with ZipFile(DATA_FOLDER + FILE_NAME, 'r') as zObject:
    zObject.extractall(path=OUTPUT_FOLDER)