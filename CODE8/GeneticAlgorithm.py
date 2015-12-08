from __future__ import unicode_literals
from __future__ import absolute_import, division
from random import uniform,randint,random,seed
from time import time
import numpy as np
from pdb import set_trace
import pickle


candidates=100
generations=1000
mutation_rate=0.05
lifes=5

"is a binary dominate b? smaller is better"
def is_bd(a,b):
    try:
        obj_a=a.getObjectives()
    except:
        obj_a=a
    try:
        obj_b=b.getObjectives()
    except:
        obj_b=b
    if obj_a==obj_b:
        return False
    for i in xrange(a.objectives):
        if obj_b[i]<obj_a[i]:
            return False
    return True

def crossover(a,b,baby):
    while True:
        x=randint(0,len(a.x))
        baby.x=list(np.array(a.x)[:x])+list(np.array(b.x)[x:])
        if baby.constraints():
            return baby

def mutate(baby):
    baby.setDecisions()
    return baby

"Update pf_best"
def compete(pf_best,pf_new):
    tmp=[]
    for a in pf_new:
        for b in pf_best:
            if is_bd(a,b):
                tmp.append(a)
                pf_best.remove(b)
    if tmp:
        pf_best.extend(tmp)
        return True
    else:
        return False

""
def init(Model,decisions=10,objectives=2,num=10000):
    can=[Model(objectives,decisions) for _ in xrange(num)]
    max=[np.max([c.getObjectives()[i] for c in can]) for i in range(objectives)]
    min=[np.min([c.getObjectives()[i] for c in can]) for i in range(objectives)]
    return min,max
    
    
"is the peddle inside the hyper volumn"
def inbox(pebble,frontier):
    for candidate in frontier:
        if is_bd(candidate,pebble):
            return True
    return False
    
    
"estimate hyper volumn of frontier"
def hve(frontier,min,max,sample=100000):
    count=0    
    print "!!!!!!! numbers in frontier::",len(frontier)
    '''
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    for i in range(len(frontier)):
        print "\n~~~~~~~~%i~~~~~~~~~" %i
        print "objectives = ", frontier[i].objectives  # No of objectives f[0]f[1],f[2],...,f[M-1]
        print "decisions  = ", frontier[i].decisions   # decision variables  
        print "domainMin  = ", frontier[i].domainMin
        print "domainMax  = ", frontier[i].domainMax
        print "x          = ", frontier[i].x
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    '''
    m=frontier[0].objectives
    #print "!!!!!!! m = ",m
    for i in xrange(sample):
        #print "Sample number",i
        #print "!!!!!!! len: min =",len(min)," max =",len(max)
        pebble=[uniform(min[k],max[k]) for k in xrange(m)]
        if inbox(pebble,frontier):
            count=count+1
    return count/(sample)


def GeneticAlgorithm(Model,decisions=10,objectives=2,DiffSeed=30):
    seed(DiffSeed)
    min,max=init(Model,decisions=decisions,objectives=objectives,num=100000)
    can=[Model(objectives,decisions) for _ in xrange(candidates)]

    pf=[]
    for a in can:
        flag=True
        for b in can:
            if is_bd(b,a):
                flag=False
                break
        if flag:
            pf.append(a)
    pf_best=pf[:]
    life=0
    for i in xrange(generations):
        can_new=[]
        for j in xrange(candidates):
            baby=Model()
            pick=np.random.choice(len(pf),2,replace=True)
            crossover(pf[pick[0]],pf[pick[1]],baby)
            if random()<mutation_rate*(2**life):
                mutate(baby)
            can_new.append(baby)
        pf_new=[]
        for a in can:
            flag=True
            for b in can:
                if is_bd(b,a):
                    flag=False
                    break
            if flag:
                pf_new.append(a)
        change=compete(pf_best,pf_new)
        if change:
            life=0
        else:
            life=life+1
        if life==lifes:
            #print "!!!!!!life = 5 breaking"
            break
        #print("Frontier num: "+str(len(pf_best)))

        can=can_new
        pf=pf_new
    
    
    solution = hve(pf_best,min,max,100000)
    return solution




