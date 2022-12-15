import turtle as t

def Shape_down(color):
    t.up()
    t.right(90)
    t.forward(120)
    t.left(90)
    t.forward(120)
    t.down()
    t.pencolor(color)
    t.circle(100)

def Shape_up(color):
    t.up()
    t.left(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.down()
    t.pencolor(color)
    t.circle(100)

t.speed(0)
t.pensize(20)
t.pencolor('blue')

t.up()
t.backward(240)
t.down()
t.circle(100)

Shape_down('yellow')
Shape_up('black')
Shape_down('green')
Shape_up('red')