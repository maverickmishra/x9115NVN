import Model
import math
import random
import copy
import sk

def SimulatedAnnealing(model):
    # print "Model: ",model.__name__
    s=model()
    sb=model()
    sb=copy.deepcopy(s)
    k = 1
    kMax=1000
    
    lives = 5 
    currentEra1 = []
    currentEra2 = []
    previousEra1 = []
    previousEra2 = []
    eraLength = 25
    
    while (k <= kMax):
        sn=neighbor(s,random.randint(0,s.decisions-1),model)
        if (type1(sn,sb)):
            sb=copy.deepcopy(sn)
            s=copy.deepcopy(sn)
        elif (type1(sn, s)):
            s=copy.deepcopy(sn)
        elif (probability(sn.eval(),s.eval(),(k/kMax))<random.uniform(0,1)):
            s=copy.deepcopy(sn)

        k = k + 1
       
        # Type 2 comparator
        if (len(currentEra1) < eraLength):
            tempVal = s.getObjectives()
            currentEra1.append(tempVal[0])
            currentEra2.append(tempVal[1])
 
        else:
            if (previousEra1 != []):
                lives += type2(previousEra1, currentEra1)
                lives += type2(previousEra2, currentEra2)

                if (lives <= 0):
                    break
            previousEra1 = list(currentEra1)  
            previousEra2 = list(currentEra2)  
            currentEra1 = []
            currentEra2 = []
                  
    return sb.x,sb.eval()

def type1(model1, model2):
    return (model1.eval() < model2.eval())
    
def type2(list1, list2):
    if (sk.a12(list1, list2) <= 0.56):
        return -1
    else:
        return 5
    
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
