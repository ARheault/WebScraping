import sys
from pathlib import Path
import os

# First we make a parent directory for data.
try:
    os.makedirs("./data")
except FileExistsError:
    # Directory is already created
    pass

'''
    Now we build directories for the specific data.
    These are done separately as to make sure each one
    is created rather than allow one FileExistsError to
    stop the other directories from being created.
'''
try:
    os.makedirs("./data/imageData")
except FileExistsError:
    # Directory is already created
    pass
try:
    os.makedirs("./data/pdfData")
except FileExistsError:
    # Directory is already created
    pass
try:
    os.makedirs("./data/webData")
except FileExistsError:
    # Directory is already created
    pass

# To place links in for the web data
try:
    linkSetup = open("./data/webData/links.txt", 'w')
    setupText = ["# For this file you will list the links of the pages you'd like to scrape\n", \
                    "# make sure to delete these lines" ]
    linkSetup.writelines(setupText)
    linkSetup.close()
except FileExistsError:
    # The file has already been setup
    pass
'''
Now we create a dump directory where we will place
all processed data. 
'''
try:
    os.makedirs("./dataDump")
except FileExistsError:
    # Directory is already created
    pass

try:
    configuration = open("config.txt", 'r+')
except:
    # If config does not exist, create it with default parameters.
    configuration = open("config.txt", 'w')
    default = \
        [
            '# Format of this file\n', \
            '# driver location ex: C:/Users/alexd/Projects/WebScraping/chromedriver.exe\n', \
            '# place 0 for disabled and 1 for enabled, default is 0 (disabled)\n', \
            'imageScraper=0\n', \
            'pdfScraper=0\n', \
            'webScraper=0\n', \
            'place driver location here'
        ]
    configuration.writelines(default)
    configuration.close()

# Now create a simple readMe.
try:
    readMe = open("readMe.txt", "w")
    lines = ["# Author: Alexander Rheault\n", \
                "# Data started: March 26th 2021\n", \
                "This file is meant to give a bit of background information as well as information about how to run the program."] 
    readMe.writelines(lines)
    readMe.close()
except FileExistsError:
    # The readMe already exists.
    pass