'''
This file will be for an image scraper. It will handle the data scraping from images.
'''

from PIL import Image
import os

# First read in all of the files in the image data directory
files = os.listdir('./data/imageData')

# For storing images in the directory
images = []

# for each file
for elem in files:
    # make sure it's an image
    if elem[-3:] == 'jpg' or elem[-3:] == 'png':
        # add it if it is, but add the path so we can open it later
        elem = os.path.dirname(os.path.realpath(__file__)) + '\\' + elem
        images.append(elem)

# Open each image
for image in images: 
    Image.open(image)