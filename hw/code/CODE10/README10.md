# x9115NVN
CSC 591 - MASE Repo

Collaborators :   
Nikhil Satish Pai   
Nikhil Anand  

# CODE 9:   
Title: Hyper Parameter Optimization   


# Abstract:   
We investigate effect of creating atleast ???? 3 options mutation, crossover, select, number of candidates and number of generations 
using Differential evolution and test the the performance of the Genetic algorithm with an untuned GA on Schaffer and Fonseca.

# Keywords:    
Genetic Algorithm, mutation, crossover, Differential Evolution, Tuning

# Main Sections:   
  A genetic algorithm is a search heuristic for solving optimization problems. They belong to a class of algorithms called evolutionary algorithms which are inspired by natural evolution techniques such as mutation, selection and crossover.
  The algorithm is as described:
    i. Randomly initialize a population
   ii. Determine the fitness of the population
  iii. Repeat until a terminating criteria is met 
       a. Select two parents from the population 
       b. Perform crossover on the parents creating a new child 
       c. Perform mutation of the population 
       d. Determine the fitness of the population
  



# Running Instructions:    
  Execute the program ------------- to view the output.     

# Results:  
  To compare the performance the Genetic algorithm with default values and tuning using a DE optimizer.
  The results are as shown below:





  Scaffer does not show any significant improvement but for Fonseca there is an improvement as shown by the diagram.   


# Threats to Validity:   
Conclusion validity
We are using a DE algorithm to optimizer to select the parameters like mutation, crossover and the results show an improvement on the Fonseca model over GA with default parameters.


Internal validity
Did the treatment/change we introduced cause the effect on the outcome? Can other factors also have had an effect?

Construct validity
Does the treatment correspond to the actual cause we are interested in? Does the outcome correspond to the effect
we are interested in?

External validity, Transferability
Is the cause and effect relationship we have shown valid in other situations? Can we generalize our results? Do the
results apply in other contexts?

Credibility
We have only tested on 2 models further testing will be needed inorder to conclusively comment on the validity of the result.

Are we confident that the findings are true? Why?
Dependability
Are the findings consistent? Can they be repeated?
Confirmalibity
Are the findings shaped by the respondents and not by the researcher?

# Future Work:   
  The current runtime is large, further optimizations may be needed to reduce the same.
  We have considered only Schaffer and Fonseca this needs to be extended to include more models    


# References:     
http://www.doc.ic.ac.uk/~nd/surprise_96/journal/vol1/hmw/article1.html
http://www.mathworks.com/discovery/genetic-algorithm.html
