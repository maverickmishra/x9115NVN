import os
import time
import math

from swampy.TurtleWorld import *

os.system('clear')

print "**********************"    
print "Output of Exercise 4.2"     
print "**********************" 

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def flower(Cursor,RADpetal,ANGpetal,NUMpetal):
    for i in range(NUMpetal):
	arc(Cursor, RADpetal, ANGpetal)
	lt(Cursor,180 - ANGpetal)
	arc(Cursor, RADpetal, ANGpetal)
	lt(Cursor, 360.0/NUMpetal)

print "********"
print "FLOWER 1"
print "********"

Frame = TurtleWorld()
Cursor = Turtle()
flower (Cursor,60,60,7)

print "********"
print "FLOWER 2"
print "********"

Frame = TurtleWorld()
Cursor = Turtle()
flower (Cursor,60,80,10)

print "********"
print "FLOWER 3"
print "********"

Frame = TurtleWorld()
Cursor = Turtle()
flower (Cursor,100,45,20)


wait_for_user()
time.sleep(10) 
