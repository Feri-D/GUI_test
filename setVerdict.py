def initVerdict():
    return ('default')


def setVerdict (finalVerdict,newVerdict):
    if (newVerdict =='pass' or newVerdict =='fail'or newVerdict =='inconclusive'):
        if (finalVerdict =='default'):
            return(newVerdict)
        if (finalVerdict=='pass'):
            return(newVerdict) 
        if (finalVerdict=='inconclusive'):
            if (newVerdict=='fail'):
                return('fail')
            return ('inconclusive')  
        if (finalVerdict=='fail'):
            return('fail')
    return ('error')

#def getVerdict():
#    return(finalVerdict)