from visual import *
from svgInator_3 import *

circles = []
radius = 20 #mm
gap = 5 #mm

dx = (radius*2)+gap

qfile = svgInator("quarto_board.svg")


side = dx*4+gap*2
outerRadius = ((2*(side**2))**0.5)/2
outerSphere = sphere(pos=(dx*2,dx*2), radius=outerRadius)

for i in range(4):
    for j in range(4):
        x = dx*i
        y = dx*j
        circles.append(sphere(pos=(x,y), radius=radius))
        qfile.writeSphere(circles[-1])

qfile.close()
        
