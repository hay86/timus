import sys, math
from decimal import *

x0, y0 = [int(x) for x in sys.stdin.readline().split()]
x1, y1 = [int(x) for x in sys.stdin.readline().split()]
x2, y2 = [int(x) for x in sys.stdin.readline().split()]

m = [[2*(x2-x0), 2*(y2-y0)],[2*(x2-x1), 2*(y2-y1)]]
v = [x2*x2+y2*y2-x0*x0-y0*y0, x2*x2+y2*y2-x1*x1-y1*y1]

if m[0][0] == 0:
	m[0], m[1] = m[1], m[0]
	v[0], v[1] = v[1], v[0]
	
k = Decimal(m[1][0]) / m[0][0]
m[1][1] -= m[0][1] * k
v[1] -= v[0] * k

k = Decimal(m[0][1]) / m[1][1]
v[0] -= v[1] * k

x = v[0] / m[0][0]
y = v[1] / m[1][1]
r = ((x-x0)*(x-x0) + (y-y0)*(y-y0)).sqrt()

def p(x, y, r):
	v = x / r
	if v < -1:
		v = -1
	if v > 1:
		v = 1
	return math.acos(v) if y>=0 else math.acos(-v) + math.pi
	
p0 = p(x0-x, y0-y, r)
p1 = p(x1-x, y1-y, r)
p2 = p(x2-x, y2-y, r)

if p0 > p1:
	p0, p1 = p1, p0
if p0 > p2:
	p0, p1 = p1 - 2*math.pi, p0
if p1 < p2:
	p0, p1 = p1, p0 + 2*math.pi

maxx = None
minx = None
maxy = None
miny = None

if p0 <= -2*math.pi <= p1 or p0 <= 0 <= p1 or p0 <= 2*math.pi <= p1:
	maxx = x+r
if p0 <= -1.5*math.pi <= p1 or p0 <= 0.5*math.pi <= p1 or p0 <= 2.5*math.pi <= p1:
	maxy = y+r
if p0 <= -math.pi <= p1 or p0 <= math.pi <= p1 or p0 <= 3*math.pi <= p1:
	minx = x-r
if p0 <= -0.5*math.pi <= p1 or p0 <= 1.5*math.pi <= p1:
	miny = y-r

if maxx == None:
	maxx = max(x0, x1)
if minx == None:
	minx = min(x0, x1)
if maxy == None:
	maxy = max(y0, y1)
if miny == None:
	miny = min(y0, y1)
	
print int((math.ceil(maxx)-math.floor(minx))*(math.ceil(maxy)-math.floor(miny)))