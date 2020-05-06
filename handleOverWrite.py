from findAndClick import findAndClick, findTarget

def overWriteRequest(sleepTime):
    if (findTarget(sleepTime,'Overwrite.png')):
        print('Archive exists already')
        findAndClick(sleepTime,'Yes.png')
        print('Overwrite confirmed')
    else:
        print('Archive does not exist yet')