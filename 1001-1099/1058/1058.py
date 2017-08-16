import sys,math

n = int(sys.stdin.readline())
a = [[None for i in range(n)] for i in range(n)]
c = []
d = [[None for i in range(n)] for i in range(n)]
half_s = 0
min_dist = sys.maxint

def eq(a, b):
	return abs(a-b) < 10**-8

def dist(i, j):
	if d[i][j] != None:
		return d[i][j]
	tmp = ((c[i][0]-c[j][0])**2 + (c[i][1]-c[j][1])**2)**0.5
	d[i][j], d[i][j] = tmp, tmp
	return tmp

def dist2(x1, y1, x2, y2):
	return ((x1-x2)**2 + (y1-y2)**2)**0.5

def area(a, b, c):
	p = (a+b+c)/2
	return (p*(p-a)*(p-b)*(p-c))**0.5

def area2(x1, y1, x2, y2, x3, y3):
	a = ((x1-x2)**2 + (y1-y2)**2)**0.5
	b = ((x1-x3)**2 + (y1-y3)**2)**0.5
	c = ((x2-x3)**2 + (y2-y3)**2)**0.5
	return area(a, b, c)

def alpha(i, j):
	if a[i][j] != None:
		return a[i][j]
	i2 = (i+1)%n
	j2 = (j+1)%n
	x0, y0 = c[i][0] - c[i2][0], c[i][1] - c[i2][1]
	x1, y1 = c[j2][0] - c[j][0], c[j2][1] - c[j][1]
	r0, r1 = (x0*x0+y0*y0)**0.5, (x1*x1+y1*y1)**0.5
	if eq(y1*x0, x1*y0):
		tmp = y0/x0 if not eq(x0, 0) else sys.maxint
	elif eq(r1*y0-r0*y1, 0):
		tmp = sys.maxint
	else:
		tmp = (r0*x1-r1*x0) / (r1*y0-r0*y1)
	a[i][j], a[j][i] = tmp, tmp
	return tmp

def abc(i, j):
	return c[j][1]-c[i][1], c[i][0]-c[j][0], -c[i][0]*(c[j][1]-c[i][1])-c[i][1]*(c[i][0]-c[j][0])

def abc2(k, i):
	if eq(k, 0):
		return 1, 0, -c[i][0]
	elif eq(k, sys.maxint):
		return 0, -1, c[i][1]
	else:
		return -1/k, -1, c[i][1]+c[i][0]/k

def xy(a1, b1, c1, a2, b2, c2):
	return (c2*b1-c1*b2)/(a1*b2-a2*b1), (c1*a2-a1*c2)/(a1*b2-b1*a2)

for i in range(n):
	x, y = [float(j) for j in sys.stdin.readline().split()]
	c.append((x, y))
	if len(c) >= 3:
		half_s += area(dist(i,i-1), dist(0,i), dist(0,i-1)) / 2

for i in range(n):
	s1, s2 = 0, 0
	for k in range(2, n):
		j1, j2 = (i+k-1)%n, (i+k)%n
		s2 = s1
		s1 += area(dist(j1,j2), dist(i,j1), dist(i,j2))
		if s1 > half_s or eq(s1, half_s):
			break
	
	k = (s1-half_s)/(half_s-s2)
	x = (c[j2][0]+k*c[j1][0]) / (k+1)
	y = (c[j2][1]+k*c[j1][1]) / (k+1)
	tmp = ((c[i][0]-x)**2 + (c[i][1]-y)**2)**0.5
	
	if min_dist > tmp:
		min_dist = tmp
#print min_dist
for i in range(n):
	s1 = 0
	i1, i2 = i, (i+1)%n
	for k in range(2, n):
		j1, j2 = (i+k-1)%n, (i+k)%n
		s1 += area(dist(j1,j2), dist(i1,j1), dist(i1,j2))
		if s1 < half_s or eq(s1, half_s):
			continue
		#print i1, i2, j1, j2

		a3, b3, c3 = abc(i1, i2)
		a4, b4, c4 = abc(j1, j2)

		#if eq(a3*b4, a4*b3) and eq(b3*c4, b4*c3):
		#	continue
	
		k = alpha(i1,j1)
		#print k
		a1, b1, c1 = abc2(k, i1)
		x1, y1 = c[i1]
		x4, y4 = xy(a1, b1, c1, a4, b4, c4)
		a2, b2, c2 = abc2(k, i2)
		x2, y2 = c[i2]
		x3, y3 = xy(a2, b2, c2, a4, b4, c4) 
		
		s2, s3 = -1, s1
		if eq(dist2(x4, y4, c[j1][0], c[j1][1]) + dist2(x4, y4, c[j2][0], c[j2][1]), dist(j1, j2)):
			s3 -= area2(x1, y1, x4, y4, c[j2][0], c[j2][1])
		else:
			a1, b1, c1 = abc2(k, j2)
			x1, y1 = xy(a1, b1, c1, a3, b3, c3)
			x4, y4 = c[j2]
			if eq(dist2(x1, y1, c[i1][0], c[i1][1]) + dist2(x1, y1, c[i2][0], c[i2][1]), dist(i1, i2)):
				s3 -= area2(x1, y1, x4, y4, c[i1][0], c[i1][1])
		if eq(dist2(x3, y3, c[j1][0], c[j1][1]) + dist2(x3, y3, c[j2][0], c[j2][1]), dist(j1, j2)):
			s2 = s3 - area2(x1, y1, x2, y2, x3, y3) - area2(x1, y1, x3, y3, x4, y4)
		else:
			a2, b2, c2 = abc2(k, j1)
			x2, y2 = xy(a2, b2, c2, a3, b3, c3)
			x3, y3 = c[j1]
			if eq(dist2(x2, y2, c[i1][0], c[i1][1]) + dist2(x2, y2, c[i2][0], c[i2][1]), dist(i1, i2)):
				s2 = s3 - area2(x1, y1, x2, y2, x3, y3) - area2(x1, y1, x3, y3, x4, y4)

		if s2 != -1 and (s2 < half_s < s3 or eq(s2, half_s) or eq(s3, half_s)):
			if eq(s3, half_s):
				tmp = dist2(x1, y1, x4, y4)
			elif eq(s2, half_s):
				tmp = dist2(x2, y2, x3, y3)
			elif eq(k, math.pi/2):
				tmp = dist2(x1, y1, x4, y4)
			else:
				d1 = dist2(x1, y1, x4, y4)
				d2 = dist2(x2, y2, x3, y3)
				k = (s3-half_s)/(half_s-s2)
				if d1 > d2:
					tmp = ((d1*d1+d2*d2*k)/(1+k))**0.5
				else:
					tmp = ((d2*d2+d1*d2/k)/(1+1/k))**0.5
			if tmp < min_dist:
				min_dist = tmp
		#print s3, s2, half_s
		#print x1, y1, x2, y2, x3, y3, x4, y4
		#print min_dist

print '%.4f' % min_dist
