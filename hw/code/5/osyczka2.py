#Osyczka2 Model implementation and related methods
from __future__ import division
import math
import random


FUNCTION_MIN = 0
FUNCTION_MAX = 0

minVector = [ 0,  0, 1, 0, 1,  0]
maxVector = [10, 10, 5, 6, 5, 10]

random.seed(8)

def rand():
    return random.random()


def function_Eval(inputVector,normalizeFlag = False):
    global FUNCTION_MIN
    global FUNCTION_MAX

    f1Sum = 25*math.pow((inputVector[0]-2),2)
    f1Sum = f1Sum + math.pow((inputVector[1]-2),2)		
    f1Sum = f1Sum + math.pow((inputVector[2]-1),2)*math.pow((inputVector[3]-4),2)		
    f1Sum = f1Sum + math.pow((inputVector[4]-1),2)
    f1 = (-1)*f1Sum
    f2 = 0
    for value in inputVector:
        f2 = f2 + math.pow(value,2) 
      
    e = f1 + f2
    if (not normalizeFlag):
        return e
    else:
        return ((e - FUNCTION_MIN)/(FUNCTION_MAX - FUNCTION_MIN))


def okConstraint(inputVector):
    if (inputVector[0] + inputVector[1] - 2 < 0):
        return False
    elif (6 - inputVector[0] - inputVector[1] < 0):
        return False
    elif (2 - inputVector[1] + inputVector[0] < 0):
        return False
    elif (2 - inputVector[0] + 3*inputVector[1] < 0):
        return False
    elif (4 - math.pow((inputVector[2]-3),2) - inputVector[3] < 0):
        return False
    elif (math.pow((inputVector[4]-3),2) + inputVector[5] - 4 < 0):
        return False
    else:
        return True

                       		
def okRange(inputVector):
    if (inputVector[0] < 0 or inputVector[0] > 10):
        return False
    elif (inputVector[1] < 0 or inputVector[1] > 10):
        return False
    elif (inputVector[2] < 1 or inputVector[2] > 5):
        return False
    elif (inputVector[4] < 1 or inputVector[4] > 5):
        return False
    elif (inputVector[3] < 0 or inputVector[0] > 6):
        return False
    elif (inputVector[5] < 0 or inputVector[5] > 10):
        return False
    return True

def generateVector():
    retVal = []
    retVal.append(random.uniform(0,10))
    retVal.append(random.uniform(0,10))
    retVal.append(random.uniform(1,5))
    retVal.append(random.uniform(0,6))
    retVal.append(random.uniform(1,5))
    retVal.append(random.uniform(0,10))
    while (not okConstraint(retVal)):
        retVal = []
        retVal.append(random.uniform(0,10))
        retVal.append(random.uniform(0,10))
        retVal.append(random.uniform(1,5))
        retVal.append(random.uniform(0,6))
        retVal.append(random.uniform(1,5))
        retVal.append(random.uniform(0,10))
    return retVal


def getRandIndex(c):
    if (c == 0 or c == 1):
        return random.uniform(0,10)
    elif (c == 2 or c == 4):
        return random.uniform(1,5)
    elif (c == 3):
        return random.uniform(0,6)
    else: 
        return random.uniform(0,10)

def baseline_study():
    global FUNCTION_MIN
    global FUNCTION_MAX
    inputVector = generateVector()
    FUNCTION_MAX = FUNCTION_MIN = function_Eval(inputVector,False)
    for index in range(10000): 
        inputVector = generateVector()
        funcOut = function_Eval(inputVector,False) 
        if (funcOut < FUNCTION_MIN):
            FUNCTION_MIN = funcOut
        if (funcOut > FUNCTION_MAX):
            FUNCTION_MAX = funcOut


def randomPart():
    return random.randint(0,5)


if __name__ != "__main__":
    baseline_study() 
    print "MIN ",FUNCTION_MIN, 
    print "MAX ",FUNCTION_MAX
