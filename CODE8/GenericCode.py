from Model import DTLZ7,Schaffer,Osyczka2,Kursawe,Golinski
from SimulatedAnnealing import SimulatedAnnealing as sa
from MaxWalkSat import MaxWalkSat as mws
from DifferentialEvolution import DifferentialEvolution as de
from utilities import rdivDemo 

#####################
import random
initSeed = 30
random.seed(initSeed)
#####################


if __name__ == '__main__':
    #for model in [DTLZ7,Schaffer,Kursawe,Osyczka2,Golinski]:
    for model in [DTLZ7]:
        rdivInput = []
        for Algorithm in [sa, mws, de]: 
            tempList = []
            tempList.append(Algorithm.__name__[:3])
            era, solution = Algorithm(model)
            for _ in solution:
                tempList.append(_)
            rdivInput.append(tempList)
    rdivDemo(rdivInput)
            

