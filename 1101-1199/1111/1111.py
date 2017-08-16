import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
	x0, y0, x1, y1 = [float(x) for x in sys.stdin.readline().split()]
	data.append((x0, y0, x1, y1))

x, y = [float(x) for x in sys.stdin.readline().split()]
ans = []

def dist(x0, y0, x1, y1):
	return ((x1-x0)**2 + (y1-y0)**2)**0.5
	
def dist2(a, b, c, x, y):
	return abs(a*x+b*y+c)/(a**2+b**2)**0.5

def foot(a, b, c, x, y):
	tmp = a**2 + b**2
	return (x*b*b-y*a*b-a*c) / tmp, (y*a*a-x*a*b-b*c) / tmp
	
for i in range(n):
	x0, y0, x2, y2 = data[i]
	if x0 == x2 and y0 == y2:
		d = dist(x, y, x0, y0)
	else:
		xm, ym = (x0+x2)/2.0, (y0+y2)/2.0
		x1, y1 = y0-ym+xm, ym+xm-x0
		x3, y3 = xm+ym-y0, x0-xm+ym
		a01, b01, c01 = y1-y0, x0-x1, x0*(y0-y1)+y0*(x1-x0)
		a12, b12, c12 = y2-y1, x1-x2, x1*(y1-y2)+y1*(x2-x1) 
		a23, b23, c23 = y3-y2, x2-x3, x2*(y2-y3)+y2*(x3-x2) 
		a03, b03, c03 = y3-y0, x0-x3, x0*(y0-y3)+y0*(x3-x0) 
		x01, y01 = foot(a01, b01, c01, x, y)
		x12, y12 = foot(a12, b12, c12, x, y)
		x23, y23 = foot(a23, b23, c23, x, y)
		x03, y03 = foot(a03, b03, c03, x, y)
		d01 = dist2(a01, b01, c01, x, y) if min(x0,x1) <= x01 <= max(x0,x1) and min(y0,y1) <= y01 <= max(y0,y1)  else sys.maxint
		d12 = dist2(a12, b12, c12, x, y) if min(x1,x2) <= x12 <= max(x1,x2) and min(y1,y2) <= y12 <= max(y1,y2)  else sys.maxint
		d23 = dist2(a23, b23, c23, x, y) if min(x2,x3) <= x23 <= max(x2,x3) and min(y2,y3) <= y23 <= max(y2,y3)  else sys.maxint
		d03 = dist2(a03, b03, c03, x, y) if min(x0,x3) <= x03 <= max(x0,x3) and min(y0,y3) <= y03 <= max(y0,y3)  else sys.maxint
		a = dist(x0, y0, x1, y1)
		if d01 <= a and d12 <= a and d23 <= a and d03 <= a:
			d = 0
		else:
			d0 = dist(x0, y0, x, y)
			d1 = dist(x1, y1, x, y)
			d2 = dist(x2, y2, x, y)
			d3 = dist(x3, y3, x, y)
			d = min(d01,d12,d23,d03,d0,d1,d2,d3)
	ans.append((i, d))

ans.sort(key=lambda x:(x[1],x[0]))
for a in ans:
	print a[0]+1,