import sys, math

n, l = [int(x) for x in sys.stdin.readline().split()]
m = []
minx, miny = sys.maxint, sys.maxint

for i in range(n):
	j = [int(x) for x in sys.stdin.readline().split()]
	m.append(j)
	if miny > j[1] or (miny == j[1] and minx > j[0]):
		minx, miny = j[0], j[1]

def cmp(a, b):
	x0, y0 = a[0]-minx, a[1]-miny
	x1, y1 = b[0]-minx, b[1]-miny
	d0, d1 = x0**2+y0**2, x1**2+y1**2
	k0, k1 = math.atan2(y0, x0), math.atan2(y1, x1)
	if k0 < 0:
		k0 += math.pi
	if k1 < 0:
		k1 += math.pi
	if k0 == k1:
		if d0 == d1:
			return 0
		else:
			return 1 if d0 > d1 else -1
	else:
		return 1 if k0 > k1 else -1
		
m.sort(cmp=cmp)

i = 0
ans = []

while i < n:
	if len(ans) < 2:
		ans.append(m[i])
		i += 1
	else:
		x0, y0 = ans[-1][0]-ans[-2][0], ans[-1][1]-ans[-2][1]
		x1, y1 = m[i][0]-ans[-2][0], m[i][1]-ans[-2][1]
		if x0*y1-x1*y0 > 0:
			ans.append(m[i])
			i += 1
		else:
			ans.pop()
			
total = 2*math.pi*l

for i in range(len(ans)):
	a, b = ans[i-1], ans[i]
	x0, y0 = a[0]-b[0], a[1]-b[1]
	total += (x0**2+y0**2)**0.5
	
print int(round(total))