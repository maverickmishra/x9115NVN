import Model
import math
import random
import copy

def SimulatedAnnealing(model):
    
    s=model()
    sb=model()
    sb=copy.deepcopy(s)
    k = 1
    kMax=1000
    linewidth=25
    printList = []
    while (k <= kMax):
        sn=neighbor(s,random.randint(0,s.decisions-1),model)
        if (sn.eval()<sb.eval()):
            sb=copy.deepcopy(sn)
            s=copy.deepcopy(sn)
            printList.append("!")  
        elif (sn.eval()<s.eval()):
            s=copy.deepcopy(sn)
            printList.append("+")
        elif (probability(sn.eval(),s.eval(),(k/kMax))<random.uniform(0,1)):
            s=copy.deepcopy(sn)
            printList.append("?")
        else:  
            printList.append(".")

        k = k + 1
        if (k % linewidth == 0):
            print "%04d," %(int(k)),
            print "  |",
            print "?=%02d" %printList.count("?"),"!=%02d" %printList.count("!"),"+=%02d" %printList.count("+"),".=%02d" %printList.count("."),
            print "  |",
            print "".join(printList)
            printList = []
            
    print "---------------------"
    print "Best solutions: "
    print "---------------------"

    for value in sb.x: print value
    return True
    
    
def neighbor(s,index,model):
    sn=model()
    sn=copy.deepcopy(s)
    while True:
        sn.x[index]=random.uniform(sn.domainMin[index],sn.domainMax[index])
        if sn.constraints(): break
    return sn
    
def probability(en,e,t):
        if t != 0:
            return math.exp((e - en )/t)