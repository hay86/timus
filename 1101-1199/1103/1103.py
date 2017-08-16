import sys

n = int(sys.stdin.readline())
m = []
a = []

for i in range(n):
	m.append([int(x) for x in sys.stdin.readline().split()])
m.sort(key=lambda x:x[1])

x1, y1 = m[0]
x2, y2 = m[1]

for i in range(2, n):
	x3, y3 = m[i]
	a1, b1, c1 = 2*(x1-x2), 2*(y1-y2), x2**2+y2**2-x1**2-y1**2
	a2, b2, c2 = 2*(x1-x3), 2*(y1-y3), x3**2+y3**2-x1**2-y1**2
	y0 = (a1*c2-a2*c1) / (a2*b1-a1*b2)
	a.append((x3, y3, y0))
	
a.sort(key=lambda x:x[2])
x3, y3, y0 = a[len(a)/2]

print x1, y1
print x2, y2
print x3, y3