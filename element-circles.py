from svgInator_2a import *
from elements_database import *

outfile = "test_circ.svg"

print He.element

n_print = 1 # "fill page" or a number

textStyle = {}
textStyle["font-size"] = "24pt"

gap = 1.0
w = 609.6
h = 457.2
s = svgInator(filename=outfile, width=w, height=h)
scale = 0.2

pos = vector(0,0)
for i in range(1, 93):
    a = get_element_by_atomic_number(i)
    radius = a.r_calculated
    print a.symbol, radius,
    if radius <> "no data":
        r = radius * scale
        pos.x = pos.x  + r + gap
        pos.y = r + gap
        
        print r, h
        j = 0

        if n_print == "fill page":
            while (j+1)*(2*r+gap)  <= h:
                
                pos.y = j*(2*r+gap) + r+gap
                s.element_circle(a.symbol, pos = pos, radius=r, textStyle=textStyle)
                j += 1
                #print pos

        else:
            for i in range(n_print):
                pos.y = j*(2*r+gap) + r+gap
                s.element_circle(a.symbol, pos = pos, radius=r, textStyle=textStyle)
                j += 1
        pos.x += r
        
    else:
        print 
#s.write(outfile)
