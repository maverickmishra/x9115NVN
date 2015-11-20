#Adding Utility functions for Type operators
from __future__ import division
import sys
import random
import math
import time
from functools import reduce
from pdb improt set_trace
import bisect

sys.dont_write_bytecode = True


#class o to be written 
class o(object):
    """ Anonymous Container """
    def __init__(self, **values):
        self.__dict__.update(values)

    def __repr__(self):
        tempDict = self.__dict__
        className = self.__class__.__name__
        return (className + '{' + ','.join(['%s: %s' %(k,tempDict[k])
                    for k in self.show()]) + '}')
        
    def show(self):
        return [key for key in sorted(self.__dict__.keys())]
        # Uncomment and modify to exclude protected and private members
        # if not "_" in key] 

def median(inputList, ordered=False):
    if not ordered:
        inputList.sort()
    listLen = len(inputList)
    if (listLen == 1):
        return inputList[0]
    elif (listLen == 2):
        return ((inputList[0] + inputList[1])/2)
    else:
        middle1 = listLen // 2
        if ((listLen & 01) == 1):
            return inputList[middle1]
        else:
            middle2 = middle1
            middle1 = middle1 - 1
            return ((inputList[middle1] + inputList[middle2])/2)

def runtime(f):
    t1 = time.time()
    f()
    return (time.time() - t1)*1000

def pairs(inputList):
    listLength = len(inputList)
    if (listLength <= 2):
        yield inputList
    else:
        for index in xrange(1,listLength):
            yield inputList[index-1], inputList[index]

def xtile(lst,lo=0,hi=100,width=50,
             chops=[0.1 ,0.3,0.5,0.7,0.9],
             marks=["-" ," "," ","-"," "],
             bar="|",star="*",show=" %3.0f"):
  """The function _xtile_ takes a list of (possibly)
  unsorted numbers and presents them as a horizontal
  xtile chart (in ascii format). The default is a 
  contracted _quintile_ that shows the 
  10,30,50,70,90 breaks in the data (but this can be 
  changed- see the optional flags of the function).
  """
  def pos(p)   : return ordered[int(len(lst)*p)]
  def place(x) : 
    return int(width*float((x - lo))/(hi - lo+0.00001))
  def pretty(lst) : 
    return ', '.join([show % x for x in lst])
  ordered = sorted(lst)
  lo      = min(lo,ordered[0])
  hi      = max(hi,ordered[-1])
  what    = [pos(p)   for p in chops]
  where   = [place(n) for n in  what]
  out     = [" "] * width
  for one,two in pairs(where):
    for i in range(one,two): 
      out[i] = marks[0]
    marks = marks[1:]
  out[int(width/2)]    = bar
  out[place(pos(0.5))] = star 
  return '('+''.join(out) +  ")," +  pretty(what)

class Num():
    def __init__(self, name, inits=[]):
        self.n = 0
        self.m2 = 0
        self.mu = 0
        self.inList = []
        self._median = None
        self.name = name
        for _ in inits:
            self.add(_)

   def standardDeviation(self):
       return (math.sqrt(self.m2)/(self.n - 1))
  
   def add(self, x):
       self._median = None
       self.n += 1
       self.inList.append(x)
       delta = x - self.mu
       self.mu += (delta*1.0)/self.n
       self.m2 += delta*(x - self.mu)

    def __add__(self, other):
        return Num(self.Name + other.Name, self.inList + other.inList)

    def quartiles(self):
        def p(x): return int(100*round(x,2))
        self.median()
        xs = self.inList
        n = int(len(xs)*0.25)
        return p(n), p(2*n), p(3*n)
             

    def median(self):
        if not self._median:
            self.inList.sort()
            self._median = median(self.inList)
        return self._median

    def __lt__(self, other):
        return (self.median() < other.median())

    def spread(self):
        self.inList.sort()
        n1 = self.n*0.25
        n2 = self.n*0.75
        if (len(self.inList) <= 1):
            return 0
        if (len(self.inList) == 2):
            return i.inList[1] - i.inList[0]
        else:
            return i.inList[int(n2)] - self.inList[int(n1)]
 


def a12(inputList1, inputList2):
    inputList1.sort()
    inputList2.sort()
    in1Len = len(inputList1)
    in2Len = len(inputList2)
    greaterCount = 0
    equalsCount = 0
    for _ in inputList1:
        leftIndex = bisect.bisect_left(inputList2, _)
        rightIndex = bisect.bisect_right(inputList2, _)
        if (leftIndex == rightIndex):
            if (leftIndex == in2Len):
                greaterCount = greaterCount + leftIndex
            elif (leftIndex == 0):
                if (inputList2[leftIndex] == _):
                    equalsCount = equalsCount + 1
            else:
                if (inputList2[leftIndex] == _):
                    equalsCount = equalsCount + 1
                greaterCount = greaterCount + leftIndex 
        else:
            greaterCount = greaterCount + leftIndex
            equalsCount = equalsCount + rightIndex - leftIndex
    return (greaterCount/(in1Len*in2Len) + equalsCount*0.5/(in1Len*in2Len))

def sampleWithReplacement(inputList):
    inListLength = len(inputList)
    retList = []
    for _ in xrange(inListLength):
        retList.append(inputList[random.randint(0,inListLength-1)])
    return retList        

def testStatistic(numContainer1, numContainer2):
    meanDiffSquared1 = 0
    meanDiffSquared2 = 0
    for _ in numContainer1.inList:
        meanDiffSquared1 += (_ - numContainer1.mu) ** 2
    for _ in numContainer2.inList:
        meanDiffSquared2 += (_ - numContainer2.mu) ** 2
    standardDeviation1 = math.sqrt(meanDiffSquared1*1.0/(numContainer1.n-1))
    standardDeviation2 = math.sqrt(meanDiffSquared2*1.0/(numContainer2.n-1))
    delta = numContainer1.mu - numContainer2.mu
    if (standardDeviation1 + standardDeviation2):
        delta = delta/math.sqrt(standardDeviation1/numContainer1 + standardDeviation2/numContainer2)   
    return delta

def bootstrap(inList1, inList2, conf=0.01, boot=1000):
    class total():
        def __init__(self, inList = []):
            self.sum = 0
            self.n = 0
            self.mu = 0
            self.All=[]
            
            for _ in some:
                self.put(_)
        def put(self,x):
            self.All.append(x)
            self.sum += x
            self.n += 1
            self.mu = self.sum*1.0/self.n
        
        def __add__(inList1, inList2):
            return total(inList1 + inList2)

    y = total(inList1)
    z = total(inList2)
    x = y + z
    tobs = testStatistic(y,z)
    yhat = [y1 - y.mu + x.mu for y1 in y.All]
    zhat = [z1 - z.mu + x.mu for z1 in z.All]
    bigger = 0.0
    for i in xrange(boot):
        if (testStatistic(total(sampleWithReplacement(yhat)),
                          total(sampleWithReplacement(zhat))) > tobs):
 
            bigger += 1
    return bigger/b < conf

def different(l1, l2):
  return a12(l2, l1) and bootstrap(l1, l2)



def scottknott(data,cohen=0.3,small=3, useA12=False,epsilon=0.01):
  """Recursively split data, maximizing delta of
  the expected value of the mean before and 
  after the splits. 
  Reject splits with under 3 items"""
  all  = reduce(lambda x,y:x+y,data)
  same = lambda l,r: abs(l.median() - r.median()) <= all.s()*cohen
  if useA12: 
    same = lambda l, r:   not different(l.all,r.all) 
  big  = lambda    n: n > small    
  return rdiv(data,all,minMu,big,same,epsilon)

def rdiv(data,  # a list of class Nums
         all,   # all the data combined into one num
         div,   # function: find the best split
         big,   # function: rejects small splits
         same, # function: rejects similar splits
         epsilon): # small enough to split two parts
  """Looks for ways to split sorted data, 
  Recurses into each split. Assigns a 'rank' number
  to all the leaf splits found in this way. 
  """
  def recurse(parts,all,rank=0):
    "Split, then recurse on each part."
    cut,left,right = maybeIgnore(div(parts,all,big,epsilon),
                                 same,parts)
    if cut: 
      # if cut, rank "right" higher than "left"
      rank = recurse(parts[:cut],left,rank) + 1
      rank = recurse(parts[cut:],right,rank)
    else: 
      # if no cut, then all get same rank
      for part in parts: 
        part.rank = rank
    return rank
  recurse(sorted(data),all)
  return data

def maybeIgnore((cut,left,right), same,parts):
  if cut:
    if same(sum(parts[:cut],Num('upto')),
            sum(parts[cut:],Num('above'))):    
      cut = left = right = None
  return cut,left,right

def minMu(parts,all,big,epsilon):
  """Find a cut in the parts that maximizes
  the expected value of the difference in
  the mean before and after the cut.
  Reject splits that are insignificantly
  different or that generate very small subsets.
  """
  cut,left,right = None,None,None
  before, mu     =  0, all.mu
  for i,l,r in leftRight(parts,epsilon):
    if big(l.n) and big(r.n):
      n   = all.n * 1.0
      now = l.n/n*(mu- l.mu)**2 + r.n/n*(mu- r.mu)**2  
      if now > before:
        before,cut,left,right = now,i,l,r
  return cut,left,right

def leftRight(parts,epsilon=0.01):
  """Iterator. For all items in 'parts',
  return everything to the left and everything
  from here to the end. For reasons of
  efficiency, take a first pass over the data
  to pre-compute and cache right-hand-sides
  """
  rights = {}
  n = j = len(parts) - 1
  while j > 0:
    rights[j] = parts[j]
    if j < n: rights[j] += rights[j+1]
    j -=1
  left = parts[0]
  for i,one in enumerate(parts):
    if i> 0: 
      if parts[i]._median - parts[i-1]._median > epsilon:
        yield i,left,rights[i]
      left += one
              

def rdivDemo(data):
  def z(x):
    return int(100 * (x - lo) / (hi - lo + 0.00001))
  data = map(lambda lst: Num(lst[0], lst[1:]),
             data)
  print ""
  ranks = []
  for x in scottknott(data, useA12=True):
    ranks += [(x.rank, x.median(), x)]
  all = []
  for _, __, x in sorted(ranks):
    all += x.all
  all = sorted(all)
  lo, hi = all[0], all[-1]
  line = "----------------------------------------------------"
  last = None
  print ('%4s , %12s ,    %s   , %4s ' %
         ('rank', 'name', 'med', 'iqr')) + "\n" + line
  for _, __, x in sorted(ranks):
    q1, q2, q3 = x.quartiles()
    print ('%4s , %12s ,    %0.2f  ,  %0.2f ' %
           (x.rank + 1, x.name, x.median(), x.spread())) + \
        xtile(x.all, lo=lo, hi=hi, width=30)
    last = x.rank
  return ranks


def fromFile(f="data.dat",rev=True,enough=0.66):
  "utility for reading sample data from disk"
  import re
  cache = {} 
  num, space = r'^\+?-?[0-9]', r'[ \t\n]+'
  for line in open(f): 
    line = line.strip()
    if line:
      for word in re.split(space,line):
        if re.match(num,word[0]):
          cache[now] += [float(word)]
        else:
          now  = word
          cache[now] = [now]
  rdivDemo(cache.values()) 


if __name__=='__main__':
  fromFile()

