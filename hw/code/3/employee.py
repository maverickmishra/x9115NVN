#Exercise on Employee class
import os

os.system('clear')

class Employee(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "%s(name='%s',age=%s)" \
                % (self.__class__.__name__,self.name,self.age)
                   
    def __lt__(self,other):
        return (self.age < other.age)

# Test for __init__
emp1 = Employee("Nikhil",25)
emp2 = Employee("Vishal",33)

# Test for __repr__
print emp1
empDup = eval(repr(emp1))
print empDup.name
print empDup.age

# Test for __lt__
print (emp1 < emp2), "expected: True"
print (emp1 == emp2), "expected: False"
print (emp1 > emp2), "expected: False"
print '' 				
