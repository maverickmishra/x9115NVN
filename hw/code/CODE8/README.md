# x9115NVN
CSC 591 - MASE Repo

Collaborators :   
Nikhil Satish Pai   
Nikhil Anand  

# CODE 8:   
# Title: Three Types of "Less Than" 

### Abstract:   
We investigate the 3 types of "Less than" operators and use them to compute the final eras of Differential Evolution, MaxWalkSat and Simulated Annealing on DTLZ7 with 2 objectives and 10 decisions and use the results to decide which among the given algorithms is the best for this model.

### Keywords:  
Bootstrap, A12, Scott Knott, Type1, Type2, Type3

### Main Sections:   
The following are the 3 optimizers being tested:    
#### 1. Simulated Annealing:  
   Simulated Annealing is an unordered search based heuristic method for solving optimization problems. It is named after a metallurgical process of heating a metal and slowly decreasing the temperature resulting in a stable structure.
   The basic algorithm consists of a decreasing series of temperatures and for each temperature a new solution is randomly generated, if the new solution is better than the current one based on a fitness function then it is accepted but if the solution is worse then the acceptance will be probabilistically depend upon the temperature parameter. This helps us to escape locally bad ideas when executing the algorithm.

#### 2. MaxWalkSat:   
   MaxWalkSat is a non-parameteric stochastic method for sampling the landscape of the local region. The intution is to mutate in all dimensions when randomly searching a search space and sometimes fixate on improving things on just one dimension. This is called as local search.
  There is also a concept of retry wherein you go back to the beginning and retry.

#### 3. Differential Evolution: 
   Differential Evolution is a method that optimizes a problem by iteratively trying to imporve a candidate solution with regards to a measure of quality. The algorithm can be optimized a large space of candidate solutions. DE does not use the gradient of the problem being optimized hence the problem need not be differentiable as is the case with classical optimization problems.
   DE optimizes a problem by maintaining a population of candidate solutions and creating new candidate solutions by combining existing ones according to its formula and keeping only those solutions which have the best score or fitness on the optimization problem. The optimization is treated as a black box that provides a measure of quality given a candidate solution and therefore does not need any gradient.
   
The following are the 3 comparision operators used in the meta heuristic algorithms:   
#### 1. Type1:     
   The Type1 comparator is used for deciding between successively generated candidate pairs of a given algorithm, For each objective which is shared between the given candidates verify if there is any improvement between the objectives, for example for a minimization problem check if each objective if lesser than the earlier generated ones. 
   This must be the fastest one in the algorithm as these will be repeatedly called in the execution of the algorithm and speed of execution of this comparision will determine the speed of the entire algorithm.

#### 2. Type2:         
   The Type2 comparator is used for deciding between set of candidates between successive eras. The outputs of two successive eras is compared to decide on early termination. An approximate heuristic is applied to performe a stats based comparision between eras, If two successive eras do not show any improvement or significant change then the algorithm is terminated early. The algorithm must be able to perform the comparision fast but not as fast as Type1 as it is not called as frequently.

  For out implementation we have choosen Krall's Bstop method. The alogrithm is as described:
    i. For each objective we start with an initial value for the lives (initialized to 5)
   ii. We run the a12 statistical significance test between the two eras
  iii. If there is no improvement in the corresponding objective we decrement the total lives by 1, if there is an improvement we increment the        number of lives by 5
   iv. If any of the objectives lives becomes 0 we terminate the algorithm.
   
   A12 Statistical Significance test:
       We have considered the Vargha and Delaney's A12 statistic.If there are m measures of X and n measures of Y it measures the probability that running algorithm X yield higher values than running algorithm Y. It specifically conunts how often larger numbers in X are seen than in Y.
```python
   a12 = (X.i > Y.j)/(n*m) + 0.5(X.i == Y.j)/(n*m) 
```
   The difference between the populations is considered to be small if the a12 stat is less than or equal to 0.56. This is used as a criteria for early termination of any algorithm.


### 2. Type3:
   The Type3 comparator is used to compare the between sets of candidate outputs from different optimizers. We will assign rankings to each of the optimizers based on the output of the optimizers.
    
  For out implementation we have choosen Saner Hypothesis Testing. The alogrithm is as described:    
+ All treatments are clustered into _ranks_. In practice, dozens
  of treatments end up generating just a handful of ranks.
+ The numbers of calls to the hypothesis tests are minimized:
    + Treatments are sorted by their median value.
    + Treatments are divided into two groups such that the
      expected value of the mean values _after_ the split is minimized;
    + Hypothesis tests are called to test if the two groups are truly difference.
          + All hypothesis tests are non-parametric and include (1) effect size tests
            and (2) tests for statistically significant numbers;
          + Slow bootstraps are executed  if the faster _A12_ tests are passed;
 


### Results:  
  The results obtained after 20 runs with a common seed generating a common baseline population across Differential Evolution, MaxWalkSat and Simulated Annealing.
![soemTExt](./img/CODE8_Results.png)


The results show that Differential evolution and MaxWalkSat rank the same whereas Simulated Annealing is not as effificient as the other two.

### Threats to Validity:   
####   i. Conclusion validity      
      The conclusions are based only on DTLZ7 with 2 objectives and 10 decisions, further testing is with more optimizers and models are needed       to validate the same.
      Algorithms for DE and Simulated Annealing generate candidate solutions randomly and the search space is also traversed randomly as a result there is no definite control over the direction of initial movement of objectives towards Heaven. 

####  ii. Internal validity     
     The Type2 operators are used to keep a track of repeated candidates in various eras and the same is being used to employ early termination of the algorithm.

#### iii. External validity            
      The experiment has been performed only on a single model hence this may be a threat as we cannot generalize the solution as it could be biased.

####  iv. Credibility               
      We are confident with out observed results as it in agreement  with conclusion of various referred literature.
 
####   v. Dependability              
      The results were measured by repeating the results for 20 runs with a different seed each time and are repeatable.

### Future Work:    

  Currently the results have been measured for DTLZ7 with 2 objectives and 10 decisions, the test must be repeated for other models to measure the performance. 
  We are currently using Boolean domination to check for early termination, further testing may be done by replacing this with Continuous domination to speedup performance.
  
### Running Instructions:    
  Execute the ["RunCode8.py"] (https://github.com/maverickmishra/x9115NVN/blob/master/hw/code/CODE8/RunCode8.py) in to view the output.     


### References:     
1. [Stats] (https://github.com/txt/mase/blob/master/STATS.md)
2. [A General Stochastic Approach to Solving Problems with Hard and Soft Constraints] (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.21.2218&rep=rep1&type=pdf)
3. [Simulated Annealing - S. Kirkpatrick and C. D. Gelatt and M. P. Vecchi Optimization by Simulated Annealing, Science, Number 4598, 13 May 1983, volume 220, 4598, pages 671680,1983] (http://minds.jacobs-university.de/sites/default/files/uploads/teaching/share/KirkpatrickSimulatedAnnealing.pdf)
4. [Differential Evolution] (http://www1.icsi.berkeley.edu/%7Estorn/code.html)
5. [DE Vs SA] (http://www.sciencedirect.com/science/article/pii/S2215098614000287)

