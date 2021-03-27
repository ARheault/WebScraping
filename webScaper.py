import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
from pathlib import Path
import os

# Check that directory for data is created
Path("./data").mkdir(parents=True, exist_ok=True)

try:
    print("MAKING DIRECTORY")
    os.makedirs("/data")
except FileExistsError:
    # Directory is already created
    pass

# Attempt to read config file.
try:
    configuration = open("config.txt", 'r+')
except:
    # If config does not exist, create it with default parameters.
    print("config not set, please read config.txt for information about setup")
    configuration = open("config.txt", 'w')
    default = \
        [
            '# Format of this file\n', \
            '# driver location ex: C:/Users/alexd/Projects/WebScraping/chromedriver.exe\n', \
            '# number of links\n', \
            'place driver location here\n', \
            'place number of links here' \
        ]
    configuration.writelines(default)
    configuration.close()
    sys.exit()

config = configuration.read().splitlines()[3:]

# Check if client has setup config.
driverPath = str(config[0])
if driverPath == 'place driver location here':
    print("Please setup configuration file, see config.txt")

# Check number of links to scrape.
numLinks = int(config[1])

# For error checking config
# print(config)

# Make sure numLinks specifies a correct number of links
if numLinks > 0:
    driver = webdriver.Chrome(executable_path=driverPath)

    try:
        for i in range(0, numLinks):
            # First for each link read in link 
            linkFile = open('link' + str(i) + '.txt', 'r')
            linkFile = linkFile.read().splitlines()[:]
            link = str(linkFile[0])

            # Now read in attributes            
            numAttr = int(linkFile[1])

            # Now read in elements
            driver.get(link)

            # Store the results here
            results = []

            content = driver.page_source

            soup = BeautifulSoup(content, 'html.parser')

            for i in range(0, numAttr):
                for elem in soup.findAll(attrs=str(linkFile[2 + i])):
                    name = elem.find(str(linkFile[2 + numAttr + i]))
                    if name not in results and name is not None:
                        # We only want non None results
                            results.append(name)

            if len(results) > 0:    
                # Clean up results (Gets rid of attribute)
                cleanResults = '\n'.join(str(results[0]).split('\n')[1:-1])

                # Write to file
                file1 = open("./data/data" + str(i) + ".txt", "w")
                for elem in cleanResults:
                    file1.writelines(elem)
                file1.close()
            else:
                # No data is scraped
                print("No data scraped, check config file for errors")
    except IndexError:
       print("IndexError, the number of links specified did not match the number of links provided.") 
else:
    print('No links to scrape, please configure the config file.')