import Model
import math
import random
import copy
import numpy
import sk

def DifferentialEvolution(model):
    # print "Model: ",model.__name__

    F=0.75
    CR=0.3
    maxtries=10
    NumCandidates=100
    best=model()
    candidates=[best]
    
    lives = 5
    currentEra1 = []
    currentEra2 = []
    previousEra1 = []
    previousEra2 = []
    eraLength = 1*NumCandidates

    
    for i in range(1,NumCandidates):
        candidate=model()
        candidates.append(candidate)
        if type1(candidate, best):
            best=copy.deepcopy(candidate)
    # print "Number Of Candidates:", len(candidates)      
    # print "Best Before TRIES in List of candidates:",best.x
    
    def mutate(candidates,F,CR,best):
        for i in range(len(candidates)):
            tmp=range(len(candidates))
            tmp.remove(i)
            while True:
                choice=numpy.random.choice(tmp,3)
                X = candidates[choice[0]]
                Y = candidates[choice[1]]
                Z = candidates[choice[2]]
                
                old=candidates[i]
                r=random.randint(0,old.decisions-1)
                new=model()
                for j in range(old.decisions):
                    if random.random()<CR or j==r:
                        new.x[j]=X.x[j] + F*(Y.x[j] - Z.x[j])  #Mutate: X + F*(Y - Z)
                    else:
                        new.x[j]=old.x[j]
                if new.constraints(): break
            if type1(new, best):
                best=copy.deepcopy(new)
            elif (not type1(new, old)):
                new=old
            yield new,best

    for tries in range(maxtries):
        newcandidates = []
        for new,best in mutate(candidates,F,CR,best):
            newcandidates.append(new)
        candidates = newcandidates

        for _ in newcandidates:
            tempVal = _.getObjectives()
            currentEra1.append(tempVal[0])
            currentEra2.append(tempVal[1])             

        if (len(currentEra1) >= eraLength):
            if (previousEra1 != []):
                lives += type2(previousEra1, currentEra1)
                lives += type2(previousEra2, currentEra2)
                if (lives <= 0):
                    return best.x,best.eval()
            previousEra1 = list(currentEra1)
            previousEra2 = list(currentEra2)
            currentEra1 = []
            currentEra2 = []
        

    return best.x,best.eval()


def type1(model1, model2):
    return (model1.eval() < model2.eval())
    
def type2(list1, list2):

    if (sk.a12(list1, list2) <= 0.56):
        return -1
    else:
        return 5
