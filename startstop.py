import os
import pyautogui
import time
import openfile
#from openfile import *
from setVerdict import *

sleepTime=1
loopTime=10
finalVerdict=initVerdict()

print('start')
openfile.openUpLogCollector()
#os.startfile ('C:\\Users\\fdemjanics\\Downloads\\esetlogcollector.exe')
time.sleep (sleepTime)
print('sleeptime')
print(pyautogui.locateCenterOnScreen('Collect.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('Collect.png'))
print('click Collect')
time.sleep (sleepTime)
if (pyautogui.locateCenterOnScreen('Overwrite.png')):
    print('Archive exists')
    finalVerdict=setVerdict(finalVerdict,'inconclusive')
    #result='inconclusive'
    time.sleep (sleepTime)
    print(pyautogui.locateCenterOnScreen('Yes.png'))
    pyautogui.click(pyautogui.locateCenterOnScreen('Yes.png'))
    print('click Yes')
else:
    print('Archive does not exist')
while((pyautogui.locateCenterOnScreen('Done.png'))==None):
    time.sleep (loopTime)
    print('wait')
else:
    print('finished')
    #time.sleep (sleepTime)
    pyautogui.click(pyautogui.locateCenterOnScreen('OK.png'))
    print('click OK')
    finalVerdict=setVerdict(finalVerdict,'pass')
time.sleep (sleepTime)
print(pyautogui.locateCenterOnScreen('Close.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('Close.png'))
print('click Close')

#pyautogui.moveTo(pyautogui.locateCenterOnScreen('Collect.png'))
#print('move')
time.sleep (sleepTime)
print (finalVerdict)
print('end')

