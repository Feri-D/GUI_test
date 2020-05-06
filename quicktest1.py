import openfile

from setVerdict import *
from handleOverWrite import overWriteRequest
from findAndClick import findAndClick, findTarget, findAndSelect

testName='quicktest1'
print('Start', testName)

i=0
sleepTime=1
loopTime=10
maxLoopCount=20
finalVerdict=initVerdict()

print('Preamble start')
openfile.openUpLogCollector()
findAndClick(sleepTime,'DefaultProfile.png')
findAndClick(sleepTime,'ProfileNone.png')
findAndSelect(sleepTime,'FirstOne.png')

print('Testbody start')
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
    print('Finished log collection successfully')
    findAndClick(sleepTime,'OK.png')
    finalVerdict=setVerdict(finalVerdict,'pass')

print('Postamble start')
findAndClick(sleepTime,'Close.png')
print ('Result: ',finalVerdict)
print ('End of', testName)