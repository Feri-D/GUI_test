from findAndClick import findAndClick, findTarget

def overWriteRequest(sleepTime):
    if (findTarget(sleepTime,'Overwrite.png')):
        print('Archive exist')
        findAndClick(sleepTime,'Yes.png')
        print('Overwrite confirmed')
    else:
        print('Archive does not exist')