import turtle

n = 60

turtle.speed('fastest')
for i in range(n):
    turtle.circle(150)
    turtle.right(360/n)

turtle.mainloop()