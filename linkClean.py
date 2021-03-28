import re


def clean(link):
    clean = link
    clean = clean.replace(":", " ")
    clean = clean.replace("//", " ")
    clean = clean.replace("/", " ")
    clean = clean.replace(".", " ")
    clean = clean.replace(":", " ")
    toClean = clean.split(' ')
    cleanList = []
    myDict = {
        'http': 0,
        'https': 0,
        'www': 0,
        'com': 0,
        'net': 0,
        'org': 0
        # not the best way, but for now it is easy and we can easily make changes to how to clean here..
    }
    for elem in toClean:
        if elem in myDict:
            continue
        else:
            cleanList.append(elem)
    clean = ''
    for i in range(0, len(cleanList)):
        if cleanList[i] != '' and i + 1 < len(cleanList):
            clean += cleanList[i] + '-'
        else:
            clean += cleanList[i]
    return clean