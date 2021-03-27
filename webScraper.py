import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import sys

# Make sure we're being passed the driver properly
if len(sys.argv) < 2:
    sys.exit()

driverPath = sys.argv[1]

# First link the driver
#driver = webdriver.Chrome(executable_path=driverPath)

# Now read link file
try:
    linkFile = open("./data/webData/links.txt", 'r')
except FileNotFoundError:
    # File isn't found
    sys.exit()

# Found the links
links = linkFile.read().splitlines()[:]
# Make sure they aren't default
if links[0] == "# For this file you will list the links of the pages you'd like to scrape" or links[1] == "# make sure to delete these lines":
    print("Check link file in ./data/webData/links.txt and follow the instructions.")

print(links)

'''
try:
    for i in range(0, numLinks):
        # First for each link read in link

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
            file1 = open("./data/webData/webData" + str(i) + ".txt", "w")
            for elem in cleanResults:
                file1.writelines(elem)
            file1.close()
        else:
            # No data is scraped
            print("No data scraped, check config file for errors")
except IndexError:
    print("IndexError, the number of links specified did not match the number of links provided.")
'''