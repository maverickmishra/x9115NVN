import os
import time
import math

from swampy.TurtleWorld import *

os.system('clear')

print "**********************"    
print "Output of Exercise 4.3"     
print "**********************" 

def drawPoly(t,n,r):
    side = 2 * r * math.sin(math.pi/n)
    midAngle = 360.0/n
    polyAngle = 180.0 - midAngle

    print "Drawing inner cuts"    
    for i in range(n-1):
        fd(t,r)
        rt(t,180)
        fd(t,r)
        lt(t,180-midAngle)

    print "Drawing Sides"
    fd(t,r)
    rt(t,90+(midAngle)/2)
    for i in range(n):
        fd(t,side)
        rt(t,midAngle)
 
print "*******"
print "SHAPE 1"
print "*******"
Frame = TurtleWorld()
Cursor = Turtle()
drawPoly(Cursor,5,100)
print "*******"
print "SHAPE 2"
print "*******"
Frame = TurtleWorld()
Cursor = Turtle()
drawPoly(Cursor,6,100)
print "*******"
print "SHAPE 3"
print "*******"
Frame = TurtleWorld()
Cursor = Turtle()
drawPoly(Cursor,7,100)

wait_for_user()
time.sleep(10) 


