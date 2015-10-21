#Max Walk Sat
from __future__ import division
import osyczka2


def mutateRand(unmutated,c):
    while True:
        unmutated[c] = osyczka2.getRandIndex(c)
        if osyczka2.okConstraint(unmutated):
            return unmutated

def mutateMaxScore(unmutated,c):
    best = list(unmutated)
    mutation = list(unmutated)
    cMax = osyczka2.maxVector[c]
    cMin = osyczka2.minVector[c]
    stepSize = (cMax - cMin)/10.0
    startIndex = cMin/10.0
    endIndex = cMax/10.0
    while cMin <= endIndex:
        mutation[c] = cMin
        if osyczka2.okRange(mutation):
            if (osyczka2.function_Eval(best,True) <= osyczka2.function_Eval(mutation,True)):
                best = list(mutation)
        cMin += stepSize        
    return best
 

def maxWalkSat(maxTries=100, maxChanges=50, p=0.5, threshold=1):
    bestVector = osyczka2.generateVector()
    count = 0
    printList = []
    for index in xrange(maxTries):
        initVector = osyczka2.generateVector()
        
        for innerIndex in xrange(maxChanges):
           if (osyczka2.function_Eval(initVector,True) > threshold):
               print "Best solution ", initVector
               print "Energy ", osyczka2.function_Eval(initVector,True)
               quit()
           
           if (osyczka2.function_Eval(initVector,True) > osyczka2.function_Eval(bestVector,True)):
               printList.append("!") 
               bestVector = list(initVector)

           c = osyczka2.randomPart()
           unmutated = list(initVector) 
           mutant = []
           if p < osyczka2.rand():
               printList.append("?") 
               mutant = mutateRand(unmutated,c)
           else:
               mutant = mutateMaxScore(unmutated,c)
               if (mutant == unmutated):
                   printList.append(".") 
               else:
                   printList.append("+")

           if len(printList) == 40:
               count += 40
               print "%03d" %count, 
               print "  |",
               print "?=%02d" %printList.count("?"),"!=%02d" %printList.count("!"),"+=%02d" %printList.count("+"),".=%02d" \
                               %printList.count("."),
               print "  |",
               print "".join(printList)
               printList = []
    
    print "Best solution:", bestVector
    print "Energy Normalized:",  osyczka2.function_Eval(bestVector,True)


maxWalkSat(100, 50, 0.5, 1)
