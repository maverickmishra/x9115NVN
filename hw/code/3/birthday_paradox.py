from __future__ import division
import os
import random


os.system("clear")

def check_duplicates (lst) :
    
    if len(lst)!=len(set(lst)):
        return True;



def ret_dupBirthdayCount(numIterations):
    occurences = 0
    for i in range(numIterations) :
        random_list = []
        for i in range(23):
            dayOfYear = random.randint(1, 365)
            random_list.append(dayOfYear)
        if check_duplicates(random_list) :
            occurences += 1
    print 'Total number of Iterations is : ', numberOfIterations
    
    print 'Number of Iterations with Duplicates is : ', occurences
    
    probability_dupBirthday = occurences/numberOfIterations
    
    print 'Probablity over a set of iterations of having a duplicate birthday among 23 students is : ', probability_dupBirthday

numberOfIterations = 50

ret_dupBirthdayCount(numberOfIterations)