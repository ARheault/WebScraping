import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
from helpers import cleaner

# Make sure we're being passed the driver
if len(sys.argv) < 2:
    sys.exit()

driverPath = sys.argv[1]

# Make sure the driver is the right format, for now we're going to check for chrome
if driverPath[len(driverPath)-16:] != 'chromedriver.exe':
    # driver not acceptable
    sys.exit()

'''
Can add an or for different browsers. Or you could set a new line to specify which browser
in the config file and use that to decide which to check.
'''

# First link the driver
driver = webdriver.Chrome(executable_path=driverPath)

'''
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
'''

# Now read link file
try:
    linkFile = open("./data/webData/links.txt", 'r')
except FileNotFoundError:
    # File isn't found
    sys.exit()

# Found the links
links = linkFile.read().splitlines()[:]
# Make sure they aren't default
if links[0] == "# For this file you will list the links of the pages you'd like to scrape" and links[1] == "# make sure to delete these lines":
    print("Check link file in ./data/webData/links.txt and follow the instructions.")

# Instantiate helpers
linkCleaner = cleaner.linkClean(0)
textCleaner = cleaner.textClean(0)

try:
    # For each link
    for link in links:
        driver.get(link)
        results = []

        # first get the contents of the page
        content = driver.page_source
        
        # use BS html parser to parse the page
        soup = BeautifulSoup(content, 'html.parser')

        # get relevant text
        text = soup.get_text()

        # Clean and format file
        text = textCleaner.clean(text)

        # Clean up link for storage name
        cleanLink = linkCleaner.clean(link)
        # Write it to a data file in the data dump
        try:
            fileSoup = open('./dataDump/' + cleanLink + '.txt', 'w')
            fileSoup.write(text)
        except FileNotFoundError:
            print("FileNotFoundError: File not found, data dump directory corrupted or deleted.")
            driver.quit()
        except:
            print("Generic Error")
            driver.quit()
except TimeoutError:
    print("Timeout")
    driver.quit()
except:
    print("generic error")
    driver.quit()
driver.quit()