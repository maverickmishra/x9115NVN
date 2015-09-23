#Helper functions for the SIMULATED ANNEALING

from __future__ import division
import random
import math
import sys
sys.dont_write_bytecode = True

#initSeed = 30
#random.seed(initSeed)

DOMAIN_MIN = -100
DOMAIN_MAX = 100

FUNCTION_MIN = 1000
FUNCTION_MAX = 0
	
def function_Eval(x,normalizeFlag = False):
    f1 = math.pow(x,2)
    f2 = math.pow((x-2),2)
    if (not normalizeFlag):
        return (f1+f2)	
    else:
        return (((f1+f2) - FUNCTION_MIN)/(FUNCTION_MAX - FUNCTION_MIN))    

def baseline_study():
    x = random.randrange(DOMAIN_MIN,DOMAIN_MAX)
    global FUNCTION_MIN
    global FUNCTION_MAX
    #FUNCTION_MAX = FUNCTION_MIN = function_Eval(x,normalizeFlag = False)
    for index in range(1000):
        x = random.random()
        funcOut = function_Eval(x,False)
        if (funcOut < FUNCTION_MIN):
            FUNCTION_MIN = funcOut
        if (funcOut > FUNCTION_MAX):
            FUNCTION_MAX = funcOut  

def prob(eInit,eNeigh,t):
    return math.e**((eInit - eNeigh )/t)
        
        
def random_num():
    return(random.random())

#def epsilon():
#    return(0.8569)

if __name__ != "__main__":
    baseline_study()
    print "FUNCTION_MIN",FUNCTION_MIN 
    print "FUNCTION_MAX",FUNCTION_MAX
#    print "Initial Seed %d" %initSeed

