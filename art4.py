from turtle import *

speed(0)
pensize(2)
degree = 2

for i in range(1,1200,3):

    forward(i)
    left(120+degree)

mainloop()