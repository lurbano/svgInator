from svgInator import *

s = svgInator("ellipseTest.svg", units="")
rx = 10
ry = 20

for i in range(10):
    x = i * 2.1* ry
    s.ellipse(rx=rx, ry=ry, pos=vector(x,0,0))
    s.ellipse(rx=rx, ry=ry, transform=f'translate({x},0), rotate(90)')
s.close()
