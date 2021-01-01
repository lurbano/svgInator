from svgInator import *

bigDim = vector(15, 10)     # (x, y) = (width, height)
gapDim = vector(2.5, 4.0)


p0 = vector(10, 10)

n = 4       # number of bonds

# relative moves
r = []
r.append( vector(0,0) )
r.append( r[-1] + vector(0, (bigDim.y-gapDim.y)/2.0) )
r.append( r[-1] + vector(gapDim.x, 0) )
r.append( r[-1] + vector(0, gapDim.y) )
r.append( r[-1] + vector(-gapDim.x, 0) )
r.append( r[-1] + vector(0, (bigDim.y-gapDim.y)/2.0) )

r2 = []
r2.append( vector(bigDim.x,0) )
r2.append( r2[-1] + vector(0, (bigDim.y-gapDim.y)/2.0) )
r2.append( r2[-1] + vector(-gapDim.x, 0) )
r2.append( r2[-1] + vector(0, gapDim.y) )
r2.append( r2[-1] + vector(+gapDim.x, 0) )
r2.append( r2[-1] + vector(0, (bigDim.y-gapDim.y)/2.0) )


s = svgInator()
pts = []

#do gaps first
for i in range(n):
    base_pos = p0 + i *vector(0, bigDim.y)
    for j in r:
        pts.append(base_pos + j)
        print pts[-1], j

s.polyline(pts)

    
s.write("bonds.svg")
