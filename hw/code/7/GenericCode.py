
from Model import Schaffer,Osyczka2,Kursawe,Golinski
from SimulatedAnnealing import SimulatedAnnealing as sa
from MaxWalkSat import MaxWalkSat as mws
from DifferentialEvolution import DifferentialEvolution as de


#####################
import random
initSeed = 30
random.seed(initSeed)
#####################


if __name__ == '__main__':
    for model in [Schaffer,Kursawe,Osyczka2,Golinski]:
        for Algorithm in [sa, mws, de]:
            print "###################################################################################"
            print "Algorithm: %s " %Algorithm.__name__
            print "Model    : %s " %model.__name__
            print "###################################################################################"
            Algorithm(model)
            print "###################################################################################"
            

