
from Model import DTLZ7,Schaffer,Osyczka2,Kursawe,Golinski
from SimulatedAnnealing import SimulatedAnnealing as sa
from MaxWalkSat import MaxWalkSat as mws
from DifferentialEvolution import DifferentialEvolution as de


#####################
import random
initSeed = 30
random.seed(initSeed)
#####################


if __name__ == '__main__':
    #for model in [DTLZ7,Schaffer,Kursawe,Osyczka2,Golinski]:
    for model in [DTLZ7]:

        for Algorithm in [sa, mws, de]:
            print "###################################################################################"
            print "Algorithm: %s " %Algorithm.__name__
            print "Model    : %s " %model.__name__
            print "###################################################################################"
            Algorithm(model)
            print "###################################################################################"
            

