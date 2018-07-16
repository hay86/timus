import sys, math

a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]
c = [int(x) for x in sys.stdin.readline().split()]
r = int(sys.stdin.readline())

x = ((a[0]-b[0])**2 + (a[1]-b[1])**2 +(a[2]-b[2])**2)**0.5
y = ((c[0]-b[0])**2 + (c[1]-b[1])**2 +(c[2]-b[2])**2)**0.5
z = ((a[0]-c[0])**2 + (a[1]-c[1])**2 +(a[2]-c[2])**2)**0.5

def acos(x):
	if x > 1:
		x = 1
	if x < -1:
		x = -1
	return math.acos(x)

if x == 0:
	print 0
else:
	p = (x+y+z)/2
	s = abs(p*(p-x)*(p-y)*(p-z))**0.5
	h = 2*s/x

	a1 = acos((x*x+z*z-y*y)/(2*x*z))
	a2 = acos((y*y+x*x-z*z)/(2*y*x))

	if h >= r or a1 >= math.pi/2 or a2 >= math.pi/2:
		print '%.2f' % round(x, 2)
	else:
		p1 = (y*y-r*r)**0.5 + (z*z-r*r)**0.5
		p2 = acos((y*y+z*z-x*x)/(2*y*z)) - acos(r/y) - acos(r/z)
		ans = p1 + p2 * r
		print '%.2f' % round(ans, 2)
