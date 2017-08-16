'''
rotate (x, y) based on center (x0, y0) with angle k click-wise
x'= (x - x0)*cos(k) + (y - y0)*sin(k) + x0 ;
y'=-(x - x0)*sin(k) + (y - y0)*cos(k) + y0 ;
'''

import sys
from math import sin, cos, radians

n = int(sys.stdin.readline())
c = []
k = []

for i in range(n):
	x0, y0 = [float(j) for j in sys.stdin.readline().split()]
	c.append((x0*100000000, y0*100000000))

for i in range(n):
	r = -radians(float(sys.stdin.readline()))
	k.append((sin(r), cos(r)))

ax, bx, cx = 1, 0, 0
ay, by, cy = 0, 1, 0
for i in range(n):
	axx = ax * k[i][1] + ay * k[i][0]
	bxx = bx * k[i][1] + by * k[i][0]
	cxx = cx * k[i][1] + cy * k[i][0] - c[i][0] * k[i][1] - c[i][1] * k[i][0] + c[i][0]
	ayy = -ax * k[i][0] + ay * k[i][1]
	byy = -bx * k[i][0] + by * k[i][1]
	cyy = -cx * k[i][0] + cy * k[i][1] + c[i][0] * k[i][0] - c[i][1] * k[i][1] + c[i][1]
	ax, bx, cx = axx, bxx, cxx
	ay, by, cy = ayy, byy, cyy

x = (cy * bx - cx * (by-1)) / ((ax-1) * (by-1) - ay * bx)
y = (cx * ay - cy * (ax-1)) / ((by-1) * (ax-1) - bx * ay)

for i in range(n):
	print round(x/100000000, 2), round(y/100000000, 2)
	xx = (x - c[i][0]) * k[i][1] + (y - c[i][1]) * k[i][0] + c[i][0]
	yy = -(x - c[i][0]) * k[i][0] + (y - c[i][1]) * k[i][1] + c[i][1]
	x, y = xx, yy
