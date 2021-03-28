# Author: Alexander Rheault
# Data started: March 26th 2021
This file is meant to give a bit of background information as well as information about how to run the program.

Steps to use program:
1. run 'python main.py'
This will begin the setup process as well as setting up directories for you to use.

2. Follow instructions given from the setup.
These instructions, incase they are unclear, are to open the new 'config.txt' file
that should now exist in the root directory. Follow the conventions set forth in the file.

3. After setting up the config file, navigate to the data directory.
In this directory you will find three data directories.

- The imageData directory is for images. You should be able to put any images you'd like data scraped from in
this directory and when you run the program it will scrape it.

- The pdfData directory is for pdfs, you should be able to put any pdf in this directory to be scraped for data.

- The webData directory is for WebScraping. There is a file that will be created by the setup called 'links.txt'.
This file is where you will place links of the websites you'd like data scraped from.

4. This program requires the use of chrome as a driver to scrape the web. For web scraping functionality you will
need to find the version of chrome you're using by navigating to settings/help in google chrome and looking at the
version number. Now you'll need to navigate to https://chromedriver.chromium.org/downloads and download the correct
webdriver for your version of google chrome.

5 is subject to change if I decide to just make it an exe
5. After the setup is complete you can run the program at any time by typing the same command 'python main.py'
The program will scrape any images in the imageData directory, and pdfs in the pdfData directory, and any websites
in the links file.
