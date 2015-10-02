#Schaffer Model

from __future__ import division
from time import strftime
import schaffer_random
import sys
sys.dont_write_bytecode = True


def simulate_Annealer():
    sInit = schaffer_random.random_number()
    eInit = schaffer_random.function_Eval(sInit,normalizeFlag = True) 
    sBest = sInit
    eBest = eInit
    
    eMax = -0.1 
    kMax = 1000
    k = 1
    printList = []
    print "### SCHAFFER FUNCTION N.1 FOR SIMULATED ANNEALING ###"
    print "#" + strftime("%Y-%m-%d %H:%M:%S") + "\nSchaffer"
    print "Initial Value: %f" %sInit
    print "Initial eng: %f" %eInit
    #sNeigh = sInit
    while (k <= kMax):
        #sNeigh = schaffer_random.random_number()
        sNeigh = schaffer_random.neigh(sInit)
        #print "Neigh:", sNeigh,
        eNeigh = schaffer_random.function_Eval(sNeigh,normalizeFlag = True)
        #print "energy:", eNeigh,
        
        if (eNeigh < eBest):
            sBest = sNeigh
            eBest = eNeigh
            printList.append("!")  
            
        if (eNeigh < eInit):
            sInit = sNeigh
            eInit = eNeigh
            printList.append("+")
        elif (schaffer_random.prob(eInit,eNeigh,(k/kMax)) < schaffer_random.random_num()):
            sInit = sNeigh
            eInit = eNeigh
            printList.append("?")
        #else:
            
        printList.append(".")
        
        #print "sbest:", sBest ,
        #print "ebest:", eBest
        
        k = k + 1
        if (k % 25 == 0):
            print "%04d," %(int(k)),
            print "  |",
            print "?=%02d" %printList.count("?"),"!=%02d" %printList.count("!"),"+=%02d" %printList.count("+"),".=%02d" %printList.count("."),
            print "  |",
            print "".join(printList)
            printList = []
    print "The best solution is %f" %sBest

simulate_Annealer()    



