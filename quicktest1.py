import os
import pyautogui
import time
import openfile
#from openfile import *
from setVerdict import *
from findAndClick import findAndClick

sleepTime=1
loopTime=10
finalVerdict=initVerdict()

print('start quicktest1')
openfile.openUpLogCollector()
findAndClick(sleepTime,'Collect.png')
print('click Collect')
time.sleep (sleepTime)
if (pyautogui.locateCenterOnScreen('Overwrite.png')):
    print('Archive exists')
    #finalVerdict=setVerdict(finalVerdict,'inconclusive')
    findAndClick(sleepTime,'Yes.png')
    print('click Yes')
else:
    print('Archive does not exist')
while((pyautogui.locateCenterOnScreen('Done.png'))==None):
    time.sleep (loopTime)
    print('wait')
else:
    print('finished')
    findAndClick(sleepTime,'OK.png')
    print('click OK')
    finalVerdict=setVerdict(finalVerdict,'pass')
findAndClick(sleepTime,'Close.png')
print('click Close')
time.sleep (sleepTime)
print (finalVerdict)
print ('end')

