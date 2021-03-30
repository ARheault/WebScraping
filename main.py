'''
This is the main execution thread of the project. It will check the config file run the
subroutines accordingly.
'''

import subprocess
import sys
from pathlib import Path
import os
import platform

# Find out which OS
whichOS = platform.system()

# Check if the config file exists.
if not os.path.exists('config.txt'):
    print("Running initial setup please refer to config.txt for information.")
    if whichOS == 'Windows':
        subprocess.run("python setup.py") 
    else:
        subprocess.run("python3 setup.py") 

# If the config does exist.
else:
    # Make sure we remove all files that aren't needed
    # commented out for development copy
    '''
    if os.path.exists('setup.py'):
        os.remove('setup.py')
    '''

    # Now read from config file and figure out what routines need to run. 
    try:
        configuration = open("config.txt", 'r+')
    except:
        print("setup was not done correctly, please try to remove and redownload a fresh copy")
        sys.exit()

    config = configuration.read().splitlines()[3:]

    if config[0][-1] == '1':
        # Use image scraper
        if whichOS == 'Windows':
            subprocess.run("python imageScraper.py")
        else:
            subprocess.run("python3 imageScraper.py")
    
    if config[1][-1] == '1':
        # use pdf  scraper
        if whichOS == 'Windows':
            subprocess.run("python pdfScraper.py")
        else:
            subprocess.run("python3 pdfScraper.py")
    
    if config[2][-1] == '1':
        # Check if client has setup config.
        driverPath = str(config[3])
        if driverPath == 'place driver location here':
            print("Please set driver location value in config.txt")
            sys.exit()
        else:
            if whichOS == 'Windows':
                    subprocess.run("python webScraper.py " + driverPath)
            else:
                    subprocess.run("python3 webScraper.py " + driverPath)