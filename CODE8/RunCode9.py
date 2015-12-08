from Model import DTLZ7,Schaffer,Osyczka2,Kursawe,Golinski
from SimulatedAnnealing import SimulatedAnnealing as sa
from MaxWalkSat import MaxWalkSat as mws
from DifferentialEvolution import DifferentialEvolution as de
from GeneticAlgorithm import GeneticAlgorithm as ga

from sk import rdivDemo 

if __name__ == '__main__':
    #numOfF=[2,4,6,8]
    #numOfX=[10,20,40]
    numOfF=[8]
    numOfX=[40]
    solutions={}
    for model in [DTLZ7]:
        solutions[model.__name__]={}
        for Algorithm in [ga]:
            print "###################################################################################"
            print "Algorithm: %s " %Algorithm.__name__
            print "Model    : %s " %model.__name__
            print "###################################################################################"
            for objectives in numOfF:
                print "Number of objectives [f(x)] : %s " %objectives
                solutions[model.__name__][objectives]={}
                for decisions in numOfX:
                    print "Number of decisions [x] : %s " %decisions
                    solutions[model.__name__][objectives][decisions]=[]
                    i = 1
                    for DifferentSeeds in xrange(20):
                        print "Iteration : ", i, "Seed = ", DifferentSeeds
                        x=Algorithm(model,decisions=decisions,objectives=objectives,DiffSeed=DifferentSeeds)
                        solutions[model.__name__][objectives][decisions].append(x)
                        i += 1
                    
            print "------------------------------------------"
            
            print "------------------------------------------"
            print "Best solutions: "
            print "~~~~~~~~~~~~~~~~~~~~~"
            n=1
            for s in solutions: 
                print "%02d" %n,":",s
                n+=1
            print "~~~~~~~~~~~~~~~~~~~~~"
                     




