# Utility script to unzip and organize hockey stats files from Kaggle
import pandas as pd
from zipfile import ZipFile

# Define variables
DATA_FOLDER = '../data/raw/'
FILE_NAME = 'archive.zip'
OUTPUT_FOLDER = '../data/interim/'

# Unzip archive folder
with ZipFile(DATA_FOLDER + FILE_NAME, 'r') as zObject:
    zObject.extractall(path=OUTPUT_FOLDER)

