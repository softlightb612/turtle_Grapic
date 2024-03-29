# file nautilus.py
"""
Draw a 'nautilus' figure
using repeated rotated and rescaled
squares.
"""

import turtle
#from utilities import saveImage

def square(T, S):
    """With turtle T,draw a square of size S."""
    for k in range(0,4):
        T.forward(S)
        T.left(90)

def repeat(T, f, N, A, S, k):
    """With turtle T, draw a figure of size S using function f N times,
    each time rotating the figure with respect to the previous one
    by an angle A and rescaling the figure by a factor k"""
    T.color('gray')
    for j in range(0, N):
        f(T, S)
        T.left(A)
        S = k*S

fred = turtle.Turtle()

turtle.bgcolor("black")

fred.speed("fastest")
repeat(fred, square, 108, 10, 200, 0.97)

turtle.done()