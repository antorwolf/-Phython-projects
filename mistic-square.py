import turtle
import random
import math

t = turtle.Turtle()

for i in range(0, 1000+1):
  t.width( math.fabs(random.randint(0,5)))
  t.goto(
  100 * math.sin(2 * math.pi * (i * 0.9 )/100.)  , 
    100 * math.sin(2 * math.pi * i/100.) )
