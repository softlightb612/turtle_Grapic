''' Code example 1
from turtle import *
color('red', 'yellow')
begin_fill()
speed('fastest')
while True:
    forward(300)
    left(170)
    if abs(pos()) < 1:  # turtle의 좌표가 원점으로부터 1픽셀 이하의 좌표이면
        break
end_fill()
done()
'''

'''Code example 2 '''
import turtle

myturtle = turtle.Turtle()
myturtle.color('red', 'yellow')
myturtle.begin_fill()
myturtle.speed('fastest')  # or slow
while True:
    myturtle.forward(300)
    myturtle.left(170)
    if abs(myturtle.pos()) < 1:# turtle의 좌표가 원점으로부터 1픽셀 이하의 좌표이면
        break
myturtle.end_fill()

turtle.done()