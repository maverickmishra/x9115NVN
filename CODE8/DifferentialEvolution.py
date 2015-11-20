import Model
import math
import random
import copy
import numpy
import utilities

def DifferentialEvolution(model):
    print "Model: ",model.__name__

    F=0.75
    CR=0.3
    maxtries=50
    NumCandidates=10
    best=model()
    candidates=[best]
    
    lives = 5 
    currentEra = []
    previousEra = []
    eraLength = 10
    
    for i in range(1,NumCandidates):
        candidate=model()
        candidates.append(candidate)
        if type1(candidate, best):
            best=copy.deepcopy(candidate)
    print "Number Of Candidates:", len(candidates)      
    print "Best Before TRIES in List of candidates:",best.x
    
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
        currentEra = [_.x for _ in newcandidates]
        if (previousEra != []):
            lives += type2(previousEra, currentEra)
            if (lives <= 0):
                return previousEra, best.x
        else:
            previousEra = list(currentEra)  
            currentEra = []

    return previousEra, best.x


def type1(model1, model2):
    return (model1.eval() < model2.eval())
    
def type2(list1, list2):

    if (utilities.a12(list1, list2) <= 0.56):
        return -1
    else:
        return 5
