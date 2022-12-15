import turtle as t
from turtle import *

t.speed('fastest')
colors = ['red','green','blue']
pensize(2)
degree = 2

for i in range(1,500):
    pencolor(colors[i%3])
    forward(i)
    left(90+degree)

mainloop()