from svgInator import *

def ft_to_mm(ft):
    return 304.8 * float(ft)

pts = []
s = mm_to_px(ft_to_mm(sqrt(2)/2))
print "s = ", s
pts.append(vector(0,0))
pts.append(vector(s,0))
pts.append(vector(0,s))
pts.append(vector(0,0))

pts2 = []
pts2.append(vector(0,0))
pts2.append(vector(mm_to_px(ft_to_mm(sqrt(3)/2)),0))
pts2.append(vector(0,mm_to_px(ft_to_mm(0.5))))
pts2.append(vector(0,0))

diag = svgInator("triangles.svg", width=500, height=500)
diag.vectorArray_to_path(pts)
diag.vectorArray_to_path(pts2)
diag.close()
