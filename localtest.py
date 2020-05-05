from setVerdict import setVerdict

finalVerdict='default'
finalVerdict = setVerdict(finalVerdict,'pass')
print (finalVerdict)
finalVerdict = setVerdict(finalVerdict,'inconclusive')
print (finalVerdict)
finalVerdict = setVerdict(finalVerdict,'fail')
print (finalVerdict)
finalVerdict = setVerdict(finalVerdict,'inconclusive')
print (finalVerdict)
finalVerdict = setVerdict(finalVerdict,'pass')
print (finalVerdict)
finalVerdict = setVerdict(finalVerdict,'test')
print (finalVerdict)