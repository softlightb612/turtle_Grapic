from turtle import *

speed(0)
colors = ['blue']
pencolor(colors[0])

for i in range(1,500,2):
    forward(i)
    left(90)

mainloop()