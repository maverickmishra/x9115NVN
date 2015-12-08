#Helper functions for the SIMULATED ANNEALING

from __future__ import division
import random
import math
import sys
sys.dont_write_bytecode = True

#initSeed = 30
#random.seed(initSeed)
FUNCTION_MIN = 0
FUNCTION_MAX = 0
DOMAIN_MIN = -100000
DOMAIN_MAX = 100000
	
def function_Eval(x,normalizeFlag = False):
    global FUNCTION_MIN
    global FUNCTION_MAX
    f1 = math.pow(x,2)
    f2 = math.pow((x-2),2)
    e = (f1+f2)
    if (not normalizeFlag):
        return 	e
    else:
        norm = ((e - FUNCTION_MIN)/(FUNCTION_MAX - FUNCTION_MIN))
        return norm    

def baseline_study():
    x = random.uniform(DOMAIN_MIN,DOMAIN_MAX) #random.random()
    global FUNCTION_MIN
    global FUNCTION_MAX
    FUNCTION_MAX = FUNCTION_MIN = function_Eval(x,False)
    for index in range(100):
        x = random.uniform(DOMAIN_MIN,DOMAIN_MAX) 
        funcOut = function_Eval(x,False)
        if (funcOut < FUNCTION_MIN):
            FUNCTION_MIN = funcOut
        if (funcOut > FUNCTION_MAX):
            FUNCTION_MAX = funcOut  

def prob(eInit,eNeigh,t):
    return math.exp((eInit - eNeigh )/t)
        
        
def random_num():
    return random.uniform(0,1)
    
def random_number():		
    x = random.uniform(DOMAIN_MIN,DOMAIN_MAX)
    return(x)
    
def neigh(x):
    return random.uniform(-10000, 10000) + x


if __name__ != "__main__":
    baseline_study()
    print "FUNCTION_MIN",FUNCTION_MIN 
    print "FUNCTION_MAX",FUNCTION_MAX
#   print "Initial Seed %d" %initSeed

