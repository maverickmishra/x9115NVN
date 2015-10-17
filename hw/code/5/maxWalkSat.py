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
 

def maxWalkSat(maxTries=1000, maxChanges=50, p=0.5, threshold=1):
    initVector = osyczka2.generateVector()
    bestVector = list(initVector)
    count = 0
    printList = []
    for index in xrange(maxTries):
        initVector = osyczka2.generateVector()
        
        for innerIndex in xrange(maxChanges):
           if (osyczka2.function_Eval(initVector,False) > threshold):
               print "The best solution is", bestVector
               print "Energy of the best solution", osyczka2.function_Eval(initVector)

               quit()
           
           c = osyczka2.randomPart()
           unmutated = list(initVector) 
           mutant = []
           if p < osyczka2.rand():
               mutant = mutateRand(unmutated,c)
               printList.append("?") 
           else:
               mutant = mutateMaxScore(unmutated,c)
               printList.append("+")
          
           if (osyczka2.function_Eval(bestVector,True) < osyczka2.function_Eval(mutant,True)):
               bestVector = list(mutant)

           elif (osyczka2.function_Eval(bestVector,True) < osyczka2.function_Eval(initVector,True)):
               bestVector = list(initVector)
 
           else:
               printList.append(".")

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
    print "Energy Normalized:",  osyczka2.function_Eval(bestVector)


maxWalkSat(100, 25, 0.5, 400)
