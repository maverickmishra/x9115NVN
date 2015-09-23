#Schaffer Model

from __future__ import division
from time import strftime
import schaffer_random
import sys
sys.dont_write_bytecode = True


def simulate_Annealer():
    sInit = schaffer_random.random_num()
    eInit = schaffer_random.function_Eval(sInit,normalizeFlag = True) 
    sBest = sInit
    eBest = eInit
    
    eMax = -1 
    kMax = 1000
    k = 1
    printList = []
    print "### SCHAFFER FUNCTION N.1 FOR SIMULATED ANNEALING ###"
    print "#" + strftime("%Y-%m-%d %H:%M:%S") + "\nSchaffer"
    print "Initial Value: %f" %sInit
    print "Initial eng: %f" %eInit

    while (k < kMax and eInit > eMax):
        sNeigh = schaffer_random.random_num()
        eNeigh = schaffer_random.function_Eval(sNeigh,normalizeFlag = True)

        if (eNeigh < eBest):
            sBest = sNeigh
            eBest = eNeigh
            printList.append("!")  
        elif (eNeigh < eInit):
            sInit = sNeigh
            eInit = eNeigh
            printList.append("+")
        elif (schaffer_random.prob(eInit,eNeigh,(k/kMax)) < schaffer_random.random_num()):
            sInit = sNeigh
            eInit = eNeigh
            printList.append("?")
        else:
            printList.append(".")
        
        k = k + 1
        if (k % 25 == 0):
            print "%04d," %(int(k)),
            print "  |",
            print "?=%02d" %printList.count("?"),"!=%02d" %printList.count("!"),"+=%02d" %printList.count("+"),".=%02d" %printList.count("."),
            print "  |",
            print "".join(printList)
            printList = []
    print "The best solution is %f:" %sBest

simulate_Annealer()    



