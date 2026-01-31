# Python program to find approximation of an ordinary differential equation using Euler's Method.

# lets right down some basics to what the method needs in order to work

# calculate the integral curve at point x0, y0 to y'= f(x, y). This approximated line will have slope f(x0, y0).

# xn+1 = xn + h
# yn+1 = yn + h*(An), where An is f(xn, yn)

# imports
import math
from dataclasses import dataclass
# from matplotlib import pyplot as plt

@dataclass
class Point:
    xn: float
    yn: float

# need a function, using dy/dx = x^2 - y^2, initial condition y(1) = 0
dydx = lambda Point : Point.xn**2 - Point.yn**2

IV = Point(1, 0)

h = 0.1 # this is step size

def solveODE(dydx, currPoint: Point, h: float):

    # take f(x,y) of current point (slope)
    An = dydx(currPoint) 

    # solve and replace Point struct with new point values
    currPoint.xn = currPoint.xn + h
    currPoint.yn = currPoint.yn + (h * An)

    return currPoint

# def main():
#     plt.figure()