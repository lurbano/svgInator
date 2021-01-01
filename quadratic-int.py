from visual import *
from svgInator_3 import *

def f(x):
    return -(x**2)/4 + x + 4

#Axes
##xaxis = curve(pos=[vector(-10,0,0),vector(10,0,0)])
##yaxis = curve(pos=[vector(0,-10,0),vector(0,10,0)])

# Gridlines
dg = 1.0
gridlines = []
for i in arange(-10, 10+dg, dg):
    gridlines.append(curve(pos=[(-10,i,0),(10,i,0)]))
    gridlines.append(curve(pos=[(i,-10,0),(i,10,0)]))
    

shapeFile = svgInator("outQuad.svg")

xmin = -10.0
xmax = 10.0
dx = 0.1

p = []
for x in arange(xmin,xmax+dx,dx):
    y = f(x)
    if y <= 10.0:
        p.append(vector(x, y, 0))

cv = curve(pos=p)

shapeFile.writeCurve(cv)
##shapeFile.writeCurve(xaxis)
##shapeFile.writeCurve(yaxis)

for i in gridlines:
    shapeFile.writeCurve(i)



shapeFile.close()
