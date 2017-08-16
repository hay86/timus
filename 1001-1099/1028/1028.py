import sys

def binary(x):
	if len(t) == 0:
		return 0
	l, r = 0, len(t)-1
	while l<r:
		m = (l+r)/2
		if t[m]<=x:
			l=m+1
		else:
			r=m-1
	return l if t[l] > x else l+1

n = int(sys.stdin.readline())
r = [0 for i in range(n)]

t = []
for i in range(n):
	line = sys.stdin.readline()
	x = int(line[0:line.index(' ')])
	p = binary(x)
	t.insert(p, x)
	r[p] += 1

for x in r:
	print x
