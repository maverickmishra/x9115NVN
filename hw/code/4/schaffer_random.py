#Helper functions for the SA

from __future__ import division
import random
import math
import sys
sys.dont_write_bytecode = True

initSeed = 25
random.seed(initSeed)

DOMAIN_MIN = -100000	
DOMAIN_MAX = 100000

FUNCTION_MIN = 0
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
    FUNCTION_MIN = function_Eval(x,normalizeFlag = False)
    global FUNCTION_MAX
    FUNCTION_MAX = function_Eval(x,normalizeFlag = False)
    for index in range(100):
        x = random.randrange(DOMAIN_MIN,DOMAIN_MAX)
        funcOut = function_Eval(x,False)
        if (funcOut < FUNCTION_MIN):
            FUNCTION_MIN = funcOut
        if (funcOut > FUNCTION_MAX):
            FUNCTION_MAX = funcOut  

def function_Eval(x,normalizeFlag = False):
    f1 = math.pow(x,2)
    f2 = math.pow((x-2),2)
    if (not normalizeFlag):
        return (f1+f2)	
    else:
        return (((f1+f2) - FUNCTION_MIN)/(FUNCTION_MAX - FUNCTION_MIN)) 

def prob(eInit,eNeigh,t):
    try:
        return (1/(math.exp((eNeigh-eInit)/t)))
    except OverflowError:
        return(random.random())
        

def random_number():
    return(random.randrange(DOMAIN_MIN,DOMAIN_MAX))

def random_num():
    return(random.random())


def epsilon():
    return(0.8569)

if __name__ != "__main__":
    baseline_study()
    print "Initial Seed %d" %initSeed

