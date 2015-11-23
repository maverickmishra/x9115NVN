import Model
import math
import random
import copy
import sk

def MaxWalkSat(model):
    
    # print "Model : ",model.__name__
    eval=0
    evalx=0
    maxtries=100
    maxchanges=50
    threshold=-10000
    p=0.5
    step=10

    lives = 5 
    currentEra1 = []
    currentEra2 = []
    previousEra1 = []
    previousEra2 = []
    eraLength = 10

    for i in range(0,maxtries):
        s=model()
        if i==0:
            sbest=model()
            sbest=copy.deepcopy(s)
        for j in range(0,maxchanges):
            eval+=1
            if s.eval()<threshold and len(previousEra1) == eraLength:
                return sbest.x,sbest.eval()

            which=random.randint(0,s.decisions-1)
            score_old=s.eval()
            if p<random.random():
                s=neighbor(s,which,model)
            else:
                s=optc(s,which,step,model)

            if type1(s, sbest):
                sbest=copy.deepcopy(s)
                evalx=eval


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

    return sbest.x,sbest.eval()
    
def type1(model1, model2):
    return (model1.eval() < model2.eval())
    
def type2(list1, list2):
    if (sk.a12(list1, list2) <= 0.56):
        return -1
    else:
        return 5


def optc(s,index,step,model):
    sn=model()
    sn=copy.deepcopy(s)
    snbest=model()
    snbest=copy.deepcopy(sn)
    dis=(sn.domainMax[index]-sn.domainMin[index])/step
    if dis != 0:
        for i in range(-int((s.x[index]-s.domainMin[index])/dis),int((s.domainMax[index]-s.x[index])/dis)+1):
            sn.x[index]=sn.x[index]+i*dis
            if not sn.constraints(): continue
            if sn.eval()<snbest.eval():
                snbest=copy.deepcopy(sn)
    return snbest
    
def neighbor(s,index,model):
    sn=model()
    sn=copy.deepcopy(s)
    while True:
        sn.x[index]=random.uniform(sn.domainMin[index],sn.domainMax[index])
        if sn.constraints(): break
    return sn
