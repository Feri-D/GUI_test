#import os
#import pyautogui
#import time
import openfile

#from openfile import *
from setVerdict import *
from handleOverWrite import overWriteRequest
from findAndClick import findAndClick, findTarget, findAndSelect

print('start quicktest1')
i=0
sleepTime=1
loopTime=10
maxLoopCount=20
finalVerdict=initVerdict()

print('preamble start')
openfile.openUpLogCollector()
findAndClick(sleepTime,'DefaultProfile.png')
findAndClick(sleepTime,'ProfileNone.png')
findAndSelect(sleepTime,'FirstOne.png')

print('testbody start')
findAndClick(sleepTime,'Collect.png')
overWriteRequest(sleepTime)

while((findTarget(loopTime,'Done.png'))==None):
    print('wait', i)
    i+=1
    if (i>maxLoopCount):
        finalVerdict=setVerdict(finalVerdict,'fail')
        print('timeout')
        break
else:
    print('finished')
    findAndClick(sleepTime,'OK.png')
    finalVerdict=setVerdict(finalVerdict,'pass')

print('postamble start')
findAndClick(sleepTime,'Close.png')
print ('Result: ',finalVerdict)
print ('quicktest1 end')