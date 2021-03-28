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
    setupText = ["# For this file you will list the links of the pages you'd like to scrape\n",
                 "# make sure to delete these lines"]
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
            '# Format of this file\n',
            '# driver location ex: C:/Users/alexd/Projects/WebScraping/chromedriver.exe\n',
            '# place 0 for disabled and 1 for enabled, default is 0 (disabled)\n',
            'imageScraper=0\n',
            'pdfScraper=0\n',
            'webScraper=0\n',
            'place driver location here'
        ]
    configuration.writelines(default)
    configuration.close()

# Now create a simple readMe.
try:
    readMe = open("readMe.txt", "w")
    lines = ["# Author: Alexander Rheault\n",
             "# Data started: March 26th 2021\n",
             "This file is meant to give a bit of background information as well as information about how to run the program.\n",
             "\n",
             "Steps to use program:\n",
             "1. run 'python main.py'\n",
             "This will begin the setup process as well as setting up directories for you to use.\n",
             "\n",
             "2. Follow instructions given from the setup.\n",
             "These instructions, incase they are unclear, are to open the new 'config.txt' file\n",
             "that should now exist in the root directory. Follow the conventions set forth in the file.\n",
             "\n",
             "3. After setting up the config file, navigate to the data directory.\n",
             "In this directory you will find three data directories.\n",
             "\n",
             "- The imageData directory is for images. You should be able to put any images you'd like data scraped from in\n",
             "this directory and when you run the program it will scrape it.\n",
             "\n",
             "- The pdfData directory is for pdfs, you should be able to put any pdf in this directory to be scraped for data.\n",
             "\n",
             "- The webData directory is for WebScraping. There is a file that will be created by the setup called 'links.txt'.\n",
             "This file is where you will place links of the websites you'd like data scraped from.\n",
             "\n",
             "4. This program requires the use of chrome as a driver to scrape the web. For web scraping functionality you will\n",
             "need to find the version of chrome you're using by navigating to settings/help in google chrome and looking at the\n",
             "version number. Now you'll need to navigate to https://chromedriver.chromium.org/downloads and download the correct\n",
             "webdriver for your version of google chrome.\n",
             "\n",
             "5 is subject to change if I decide to just make it an exe\n,"
             "5. After the setup is complete you can run the program at any time by typing the same command 'python main.py'\n",
             "The program will scrape any images in the imageData directory, and pdfs in the pdfData directory, and any websites\n",
             "in the links file."]
    readMe.writelines(lines)
    readMe.close()
except FileExistsError:
    # The readMe already exists.
    pass
