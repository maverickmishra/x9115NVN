# x9115NVN
CSC 591 - MASE Repo

Collaborators :   
Nikhil Satish Pai   
Nikhil Anand  

# CODE 8:   
Title: Three Types of "Less Than"  

# Abstract:   
We investigate the 3 types of "Less than" operators and use them to compute the final eras of Differential Evolution, MaxWalkSat and Simulated Annealing on DTLZ7 with 2 objectives and 10 decisions and use the results to decide which among the given algorithms is the best for this model.

# Keywords:  
Bootstrap, A12, Scott Knott, Type1, Type2, Type3

# Introduction:   





# Main Sections:   
The following are the 3 comparision operators used in the meta heuristic algorithms:   
1. Type1:     
   The Type1 comparator is used for deciding between successively generated candidate pairs of a given algorithm, For each objective which is shared between the given candidates verify if there is any improvement between the objectives, for example for a minimization problem check if each objective if lesser than the earlier generated ones. 
   This must be the fastest one in the algorithm as these will be repeatedly called in the execution of the algorithm and speed of execution of this comparision will determine the speed of the entire algorithm.

2. Type2:         
   The Type2 comparator is used for deciding between set of candidates between successive eras. The outputs of two successive eras is compared to decide on early termination. An approximate heuristic is applied to performe a stats based comparision between eras, If two successive eras do not show any improvement or significant change then the algorithm is terminated early. The algorithm must be able to perform the comparision fast but not as fast as Type1 as it is not called as frequently.

  For out implementation we have choosen Krall's Bstop method. The alogrithm is as described:
    i. For each objective we start with an initial value for the lives (initialized to 5)
   ii. We run the a12 statistical significance test between the two eras
  iii. If there is no improvement in the corresponding objective we decrement the total lives by 1, if there is an improvement we increment the        number of lives by 5
   iv. If any of the objectives lives becomes 0 we terminate the algorithm.
   
   A12 Statistical Significance test:
       We have considered the Vargha and Delaney's A12 statistic.If there are m measures of X and n measures of Y it measures the probability that running algorithm X yield higher values than running algorithm Y. It specifically conunts how often larger numbers in X are seen than in Y.
#  a12 = (X.i > Y.j)/(n*m) + 0.5(X.i == Y.j)/(n*m)
   The difference between the populations is considered to be small if the a12 stat is less than or equal to 0.56


2. Type3:
         
   





# Result:  



# Conclusions and Future Work:   




# References:     
