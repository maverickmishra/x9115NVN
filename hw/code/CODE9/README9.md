# x9115NVN
CSC 591 - MASE Repo

Collaborators :   
Nikhil Satish Pai   
Nikhil Anand  

# CODE 9:   
Title: Simplified Standard Genetic Algorithm

# Abstract:   

We investigate the performance of a standard genetic algorithm on DTLZ1,3,5,7 and compare their performance with varying objectives and decisions. 


# Keywords:    
Genetic Algorithm, mutation, crossover

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
  To compare the performance of each of the optimizers we have used the hypervolume as the measure. The each model was run 10 times, calculating the hypervolume for each run.

# Threats to Validity:   
Conclusion validity
Does the treatment/change we introduced have a statistically significant effect on the outcome we measure?
Internal validity
Did the treatment/change we introduced cause the effect on the outcome? Can other factors also have had an effect?
Construct validity
Does the treatment correspond to the actual cause we are interested in? Does the outcome correspond to the effect
we are interested in?
External validity, Transferability
Is the cause and effect relationship we have shown valid in other situations? Can we generalize our results? Do the
results apply in other contexts?
Credibility
Are we confident that the findings are true? Why?
Dependability
Are the findings consistent? Can they be repeated?
Confirmalibity
Are the findings shaped by the respondents and not by the researcher?

# Future Work:   
  The current runtime is large, further optimizations may be needed to reduce the same.
  Tuning the parameters of the GA to test the performance 
  Currently we have implemented boolean domination to compare points along the perato frontier but this does not scale well with increase in objectives and also it provides only a qualitative measure for the domination.
  SUM OF ALL SCORES ???


# References:     
http://www.doc.ic.ac.uk/~nd/surprise_96/journal/vol1/hmw/article1.html
http://www.mathworks.com/discovery/genetic-algorithm.html
