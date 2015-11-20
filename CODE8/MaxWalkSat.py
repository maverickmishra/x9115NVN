import Model
import math
import random
import copy

def MaxWalkSat(model):
    
    print "Model: ",model.__name__

    eval=0
    evalx=0
    maxtries=100
    maxchanges=50
    threshold=-10000
    p=0.5
    step=10
    # count = 0
    # linewidth = 50

    lives = 5 
    currentEra = []
    previousEra = []
    eraLength = 10

    for i in range(0,maxtries):
        s=model()
        if i==0:
            sbest=model()
            sbest=copy.deepcopy(s)
        # printList = []
        for j in range(0,maxchanges):
            eval+=1
            if s.eval()<threshold and len(previousEra) == eraLength:
                # print ""
                # print "The best solution is \n %s" %s.x
                return previousEra, sbest

            which=random.randint(0,s.decisions-1)
            score_old=s.eval()
            if p<random.random():
                s=neighbor(s,which,model)
            else:
                s=optc(s,which,step,model)

            if type1(s, sbest):
                sbest=copy.deepcopy(s)
                evalx=eval
                # printList.append("!")  
            # elif s.eval()<score_old:
                # printList.append("+")  
            # elif s.eval()==score_old:
                # printList.append("?") 
            # else:
            #    printList.append(".") 

            # count += 1
            # Type 2 comparator
            if (len(currentEra) < eraLength):
                currentEra.append(s) 
            else:
                if (previousEra != []):
                    lives += type2(previousEra, currentEra)
                    if (lives <= 0):
                        return previousEra, sbest
                else:
                    previousEra = list(currentEra)  
                    currentEra = []

            """
            if (count % linewidth == 0):        
        #if len(printList) == linewidth:
                print "%04d," %count,
                print "  |",
                print "?=%02d" %printList.count("?"), "!=%02d" %printList.count("!"),"+=%02d" %printList.count("+"),".=%02d" %printList.count("."),
                print "  |",
                print "".join(printList)
                printList = []
            """
    """
    print "---------------------"
    print "Best solutions: "
    print "---------------------"

    for value in sbest.x: 
        print value
    """
    return previousEra, sbest
    
def type1(model1, model2):
    return (model1.eval() < model2.eval())
    
def type2(list1, list2):
    if (a12(list1, list2) <= 0.56):
        return -1
    else
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
