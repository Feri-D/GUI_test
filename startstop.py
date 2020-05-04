import os
import pyautogui
import time

sleepTime=5
loopTime=10
result=['pass','fail','inconclusive']

print('start')
os.startfile ('C:\\Users\\fdemjanics\\Downloads\\esetlogcollector.exe')
time.sleep (sleepTime)
print('sleeptime')
print(pyautogui.locateCenterOnScreen('Collect.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('Collect.png'))
print('click Collect')
time.sleep (sleepTime)
if (pyautogui.locateCenterOnScreen('Overwrite.png')):
    print('Archive exists')
    result='inconclusive'
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
    result='pass'
time.sleep (sleepTime)
print(pyautogui.locateCenterOnScreen('Close.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('Close.png'))
print('click Close')

#pyautogui.moveTo(pyautogui.locateCenterOnScreen('Collect.png'))
#print('move')
time.sleep (sleepTime)
#os.system('TASKKILL /IM esetlogcollector.exe')
print(result)
print('end')

