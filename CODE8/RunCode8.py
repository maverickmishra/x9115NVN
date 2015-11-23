from Model import DTLZ7,Schaffer,Osyczka2,Kursawe,Golinski
from SimulatedAnnealing import SimulatedAnnealing as sa
from MaxWalkSat import MaxWalkSat as mws
from DifferentialEvolution import DifferentialEvolution as de
from sk import rdivDemo 

#####################
#import random
#initSeed = 55
#random.seed(initSeed)
#####################


if __name__ == '__main__':
    #for model in [DTLZ7,Schaffer,Kursawe,Osyczka2,Golinski]:
    for model in [DTLZ7]:
        rdivInput = [[],[],[]]
        rdivInput[0].append("sa ")
        rdivInput[1].append("mws")
        rdivInput[2].append("de ")
        for j in range(20):
            for Algorithm in [sa, mws, de]: 
                print "Round:" , j

            
                if Algorithm.__name__ == 'SimulatedAnnealing':
                    i = 0
                if Algorithm.__name__ == 'MaxWalkSat':
                    i = 1
                if Algorithm.__name__ == 'DifferentialEvolution':
                    i = 2

                solution,enegry = Algorithm(model)
                
                print "------------------------------------------"
                print "Model     : ",model.__name__
                print "Algorithm : ",Algorithm.__name__
                print "------------------------------------------"
                print "Best solutions: "
                print "~~~~~~~~~~~~~~~~~~~~~"
                n=1
                for x in solution: 
                    print "%02d" %n,":",x
                    n+=1
                print "~~~~~~~~~~~~~~~~~~~~~"
                print "Energy Evaluation: "
                print "~~~~~~~~~~~~~~~~~~~~~"
                print enegry
                print "~~~~~~~~~~~~~~~~~~~~~"
                rdivInput[i].append(enegry)
        rdivDemo(rdivInput)
            