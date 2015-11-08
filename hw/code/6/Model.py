import math
import random
import copy

class Model(object):
    def __init__(self):
        self.domainMin=[0]
        self.domainMax=[0]
        self.decisions=0
        self.objectives=0
        self.x=[0]

    def eval(self):
        return sum(self.getObjectives())

    def getObjectives(self):
        return []

    def setDecisions(self):
        while True:
            for i in range(0,self.decisions):
                self.x[i]=random.uniform(self.domainMin[i],self.domainMax[i])
            if self.constraints(): break

    def constraints(self):
        for i in range(0,self.decisions):
            if self.x[i]<self.domainMin[i] or self.x[i]>self.domainMax[i]:
                return False
        return True

class Schaffer(Model):
    def __init__(self):
        self.domainMin=[-100000]
        self.domainMax=[100000]
        self.decisions=1
        self.objectives=2
        self.x=[0]
        self.setDecisions()

    def getObjectives(self):
        f1=math.pow(self.x[0],2)
        f2=math.pow((self.x[0]-2),2)
        return [f1,f2]

class Osyczka2(Model):
    def __init__(self):
        self.domainMin=[0,0,1,0,1,0]
        self.domainMax=[10,10,5,6,5,10]
        self.decisions=6
        self.objectives=2
        self.x=[0,0,0,0,0,0]
        self.setDecisions()

    def getObjectives(self):
        f1=(-1)*(25*math.pow((self.x[0]-2),2)+math.pow((self.x[1]-2),2)+(math.pow((self.x[2]-1),2))*math.pow((self.x[3]-4),2)+math.pow((self.x[4]-1),2))
        f2=math.pow(self.x[0],2)+math.pow(self.x[1],2)+math.pow(self.x[2],2)+math.pow(self.x[3],2)+math.pow(self.x[4],2)+math.pow(self.x[5],2)
        return [f1,f2]

    def constraints(self):
        if (self.x[0] + self.x[1]  - 2 < 0) :
            return False
        elif (6 - self.x[0] - self.x[1] < 0) :
            return False
        elif (2 - self.x[1] + self.x[0] < 0) :
            return False
        elif (2 - self.x[0] + 3*self.x[1] < 0)  :
            return False
        elif (4 - math.pow((self.x[2]-3),2) - self.x[3] < 0) :
            return False
        elif (math.pow((self.x[4]-3),3) + self.x[5]  -  4 < 0)  :
            return False
        else:
            for i in range(0,self.decisions):
                if self.x[i]<self.domainMin[i] or self.x[i]>self.domainMax[i] :
                    return False
            return True


class Kursawe(Model):
    def __init__(self):
        self.domainMin=[-5,-5,-5]
        self.domainMax=[5,5,5]
        self.decisions=3
        self.objectives=2
        self.x=[0,0,0]
        self.setDecisions()

    def getObjectives(self):
        f1=0
        f2=0
        for i in range(0,self.decisions):
            if i<self.decisions-1:
                f1+=(-10)*math.pow(math.exp(1),(-0.2*math.sqrt(math.pow(self.x[i],2)+math.pow(self.x[i+1],2))))
            f2+=math.pow(math.fabs(self.x[i]),0.8)+5*math.sin(self.x[i])
        return [f1,f2]

def neighbor(s,index,model):
    sn=model()
    sn=copy.deepcopy(s)
    while True:
        sn.x[index]=random.uniform(sn.domainMin[index],sn.domainMax[index])
        if sn.constraints(): break
    return sn