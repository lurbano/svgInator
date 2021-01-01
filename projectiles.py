from PotatoShooting import*
from svgInator import *
scene.range=50
scene.autoscale= False
'''
a= -9.8                             #m/s^2
v= 20                               #m/s
x=0
y=0
degree= 30
dt= 0.01
'''

v=20

# get outline off maximum heights
##pts = []
##for i in range(181):
##    test = PotatoShooting(v, deg=i, dt=.1)
##    pts.append(test.maxHeight())
##diagram.vectorArray_to_path(pts)




# get flight paths
degree= 55.0

diagram = svgInator()
test= PotatoShooting(v, deg=degree, dt=.1)
test.positionXY()
diagram.writeCurve(test.ball.trail_object)
test.ball.pos.y += 20
diagram.writeSphere(test.ball)

b = box(pos=test.ball.pos - vector(0,20,0), size=(3,9,12), axis=(1,1,0))
print b.axis, b.size
diagram.writeBox(b)

diagram.close()





