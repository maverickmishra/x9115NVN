import os

##Code 2:Coding Homework
os.system('clear')

#print "**********************"    
#print "Output of Exercise 3.1"     
#print "**********************"    

#repeat_lyrics()
#
#def print_lyrics():
#    print "I'm a lumberjack, and I'm okay."
#    print "I sleep all night and I work all day."
#
#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()

os.system('clear')
print "**********************"    
print "Output of Exercise 3.2"     
print "**********************" 

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()

os.system('clear')
print "**********************"    
print "Output of Exercise 3.3"     
print "**********************" 

def right_justify(s):
    length = len(s)
    space = 70 - length -1
    print " "*space,s
#    print "{:>70}".format(s)
#    print '%70s' % s
    
right_justify("allen")
right_justify("Nikhil Anand")
right_justify("Nikhil Pai")
right_justify("Vishal Mishra")

os.system('clear')
print "**********************"    
print "Output of Exercise 3.4"     
print "**********************" 

def do_twice(f,value):
    f(value)
    f(value)
    
def print_spam():
    print 'spam'
    
def print_somevalue (value):
     print value

def print_twice(value):
    print"print_twice function called..."
    print value
    print value
    
#print_twice("passedValue")

#do_twice(print_twice,"spam")

def do_four(f,value):
    do_twice(f,value)
    do_twice(f,value)

do_four(print_twice,"spam")


os.system('clear')
print "**********************"    
print "Output of Exercise 3.5"     
print "**********************" 


def grid(r,c):
    poss = 0
    for i in range (0,r*5+1):
        if (i % 5 == 0):
            for j in range (0,c*5+1):
                if (j % 5 == 0):
                    print "+ ",
                else :
                    print "- ",
        else :
            for j in range (0,c*5+1):
                if (j % 5 == 0):
                    print "| ",
                else :
                    print "  ",  
        print ""

print "2x2 GRID:" 
grid(2,2)
print "4x4 GRID:" 
grid(4,4)

























