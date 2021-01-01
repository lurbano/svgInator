from visual import *
from svgInator_3 import *

length = 424.2  #mm
width = 454.5   #mm
nLines = 19
dx = length/(nLines-1)
dy = width/(nLines-1)

print "Lenght = ", length
print "dx = ", dx

f = svgInator("go_board.svg")

lineStyle = {"stroke": "#000", "stroke-width": "2pt",}

#lines
for i in range(nLines):
    x = i * dx
    y = i * dy
    #vertical
    f.line(pos=[vector(x,0), vector(x,width)], style=lineStyle)
    #horizontal
    f.line(pos=[vector(0,y), vector(length,y)], style=lineStyle)

#circles
grid_pos = [(3,3), (3,9), (3,15),
            (9,3), (9,9), (9,15),
            (15,3), (15,9), (15,15)]

for i in grid_pos:
    (x, y) = (i[0]*dx, i[1]*dy)
    f.circle(pos=vector(x,y), radius=2.0,
             style={"stroke": "#000", "fill":"#000"})

#bounding box
f.rect(dim=vector(length,width), style=lineStyle)

f.close()
    
