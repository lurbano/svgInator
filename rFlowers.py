from vpython import *
from svgInator import *
import random

outFile = "outRad.svg"

def f(theta):
    r = 3 * sin(theta)
    x = r * cos(theta)
    y = r * sin(theta)
    return (x, y)

def ff(theta, a = 5, n = 4):
    r = a * cos(n * theta)
    x = r * cos(theta)
    y = r * sin(theta)
    return (x, y)

def ffr(theta, a = 5, n = 4, rf=0.05):
    r = a * cos(n * theta) + (random.random() - 0.5) * a * rf
    x = r * cos(theta)
    y = r * sin(theta)
    return (x, y)

#Axes
##xaxis = curve(pos=[vector(-10,0,0),vector(10,0,0)])
##yaxis = curve(pos=[vector(0,-10,0),vector(0,10,0)])

# Gridlines
dg = 1.0
gridlines = []
for i in arange(-10, 10+dg, dg):
    gridlines.append(curve(pos=[(-10,i,0),(10,i,0)]))
    gridlines.append(curve(pos=[(i,-10,0),(i,10,0)]))


shapeFile = svgInator(outFile)

xmin = 0
xmax =  pi
dx = xmax/100

cv = curve()

p = []
for theta in arange(xmin,xmax+dx,dx):
    (x, y) = ffr(theta, a= 10, n=5, rf=0.05)
    x = round(x, 2)
    y = round(y, 2)
    if y <= 10.0 and y >= -10.0:
        p.append(vector(x, y, 0))
        cv.append(pos=vector(x,y,0))
        sleep(0.01)



shapeFile.vectorArray_to_path(p, rounding=2)
##shapeFile.writeCurve(xaxis)
##shapeFile.writeCurve(yaxis)

# for i in gridlines:
#     shapeFile.writeCurve(i)



shapeFile.close()
