import Model
import math
import random
import copy
import numpy

def DifferentialEvolution(model):
    print "Model: ",model.__name__

    nb=100
    maxtries=10
    f=0.75
    cr=0.3
    best=model()
    candidates=[best]
    for k in candidates : print "VAlues:",k.x
    
    for i in range(1,nb):
        x=model()
        candidates.append(x)
        if x.eval()<best.eval():
            best=copy.deepcopy(x)
    print "count :", len(candidates)      
    #print "BEST BEFORE TRIES :",best.x
    
    def mutate(candidates,f,cr,best):
        for i in range(len(candidates)):
            tmp=range(len(candidates))
            tmp.remove(i)
            while True:
                choice=numpy.random.choice(tmp,3)
                #print "choice",choice
                X = candidates[choice[0]]
                Y = candidates[choice[1]]
                Z = candidates[choice[2]]
                
                old=candidates[i]
                #print "~~~~old",old.x
                r=random.randint(0,old.decisions-1)
                new=model()
                for j in range(old.decisions):
                    if random.random()<cr or j==r:
                        new.x[j]=X.x[j]+f*(Y.x[j]-Z.x[j])  #Mutate: X + F*(Y - Z)
                    else:
                        new.x[j]=old.x[j]
                if new.constraints(): break
            if new.eval()<best.eval():
                best=copy.deepcopy(new)
                printList.append("!")
                #printList.append (str(best.x)) ##New Best Found
            elif new.eval()<old.eval():
                printList.append("+")
            else:
                new=old
                printList.append(".")
            #print "~~~~new",new.x
            yield new,best

    for tries in range(maxtries):
        printList = []
        print "Tries:",tries,
        print "|",
        newcandidates = []
        for new,best in mutate(candidates,f,cr,best):
            newcandidates.append(new)
        candidates = newcandidates
        print "!=%02d" %printList.count("!"),"+=%02d" %printList.count("+"),".=%02d" %printList.count("."),
        print "  |",
        print "".join(printList)

        print("")
    print "---------------------"
    print "Best solutions: "
    print "---------------------"
    for value in best.x: 
        print value


