# base class for cleaning
class cleaner:
   pass

class linkClean(cleaner):
    def __init__(self, setting):
        # setting will be used to figure out how much we want to clean
        self.setting = setting

    def clean(self, link):
        clean = link
        # first replace all delimiters with spaces and break it into a list
        toClean = clean.replace(":", " ").replace("//", " ").replace("/", " ").replace(".", " ").replace(":", " ").split(' ')

        cleanList = []
        myDict = {
            'http': 0,
            'https': 0,
            'www': 0,
            'com': 0,
            'net': 0,
            'org': 0
            # Can add new values that you'd like to remove from here.
            # Add a comma to the value before and format is
            # 'thingToIgnore': 0
        }
        # If it's not in the specified works to remove add it to the clean list
        for elem in toClean:
            if elem in myDict:
                continue
            else:
                cleanList.append(elem)
        # Change list into string
        # Using join had a None value for some reason at the start, so for now this
        # but I'd like to 
        clean = ''
        for i in range(0, len(cleanList)):
            if cleanList[i] != '' and i + 1 < len(cleanList):
                clean += cleanList[i] + '-'
            else:
                clean += cleanList[i]
        return clean   

class textClean(cleaner):
    def __init__(self, setting):
        # setting will be used to figure out how much we want to clean
        self.setting = setting
    
    def clean(self, text):
        toClean = text.split('\n')
        clean = ''
        for elem in toClean:
            if elem is not None and elem != '':
                clean += elem + '\n'
        return clean