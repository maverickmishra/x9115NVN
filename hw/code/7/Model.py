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
        self.__name__ = 'schaffer'

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
        self.__name__ = 'Osyczka2'


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
        self.__name__ = 'Kursawe'

    def getObjectives(self):
        f1=0
        f2=0
        for i in range(0,self.decisions):
            if i<self.decisions-1:
                f1+=(-10)*math.pow(math.exp(1),(-0.2*math.sqrt(math.pow(self.x[i],2)+math.pow(self.x[i+1],2))))
            f2+=math.pow(math.fabs(self.x[i]),0.8)+5*math.sin(self.x[i])
        return [f1,f2]
        
        
        
class Golinski(Model):
    def __init__(self):
        self.domainMin=[2.6,0.7,17.0,7.3,7.3,2.9,5.0]
        self.domainMax=[3.6,0.8,28.0,8.3,8.3,3.9,5.5]
        self.decisions=7
        self.objectives=2
        self.x=[0,0,0,0,0,0,0]
        self.setDecisions()
        self.__name__ = 'Golinski'
        
    def getObjectives(self):
        f1=(0.7854)*self.x[0]*math.pow(self.x[1],2)*(10/3*math.pow(self.x[2],2)+(14.933)*self.x[2]-43.0934)-(1.508)*self.x[0]*(math.pow(self.x[6],2)+math.pow(self.x[5],2))+(7.477)*(math.pow(self.x[6],3)+math.pow(self.x[5],3))+(0.7854)*(self.x[3]*math.pow(self.x[5],2)+self.x[4]*math.pow(self.x[6],2))
        f2=math.sqrt(math.pow((745*self.x[3]/self.x[1]/self.x[2]),2)+(1.69)*math.pow(10,7))*10/math.pow(self.x[5],3)
        return [f1,f2]



    def constraints(self):
        a = 745 * (self.x[4] / (self.x[1] * self.x[2]))
        b = 1.575 * (10 ** 8)

        if (((1.0 / (self.x[0] * (self.x[1] ** 2) * self.x[2])) - (1.0 / 27)) > 0):
            return False
        elif (((self.x[3] ** 3) / (self.x[1] * (self.x[2] ** 2) * (self.x[5] ** 4))) - (1 / 1.93) > 0):
            return False
        elif (((self.x[4] ** 3) / (self.x[1] * self.x[2] * (self.x[6] ** 4))) - (1 / 1.93) > 0):
            return False
        elif ((self.x[1] * self.x[2]) - 40 > 0):
            return False
        elif ((self.x[0] / self.x[1]) - 12 > 0):
            return False
        elif (5 - (self.x[0] / self.x[1]) > 0):
            return False
        elif (1.9 - self.x[3] + 1.5 * self.x[5] > 0):
            return False
        elif (1.9 - self.x[4] + 1.1 * self.x[6] > 0):
            return False
        elif (self.getObjectives()[1] > 1300):
            return False
        elif (math.sqrt((a ** 2) + (b ** 2)) / (0.1 * (self.x[2] ** 7)) > 1100):
            return False
        else:
            for i in range(0,self.decisions):
                if self.x[i]<self.domainMin[i] or self.x[i]>self.domainMax[i] :
                    return False
        return True


def neighbor(s,index,model):
    sn=model()
    sn=copy.deepcopy(s)
    while True:
        sn.x[index]=random.uniform(sn.domainMin[index],sn.domainMax[index])
        if sn.constraints(): break
    return sn
