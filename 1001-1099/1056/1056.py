import sys

n = int(sys.stdin.readline())
e = {}
l = {1:1}
e1 = 1
e2 = 1
m = 0

def dist(a, b):
	if l[a] > l[b]:
		a, b = b, a
	d = l[b] - l[a]
	for i in range(d):
		b = e[b]
	while a != b:
		a = e[a]
		b = e[b]
		d += 2
	return d

for i in range(2, n+1):
	p = int(sys.stdin.readline())
	e[i] = p
	l[i] = l[p] + 1
	m1 = dist(e1, i)
	m2 = dist(e2, i)
	(mm, me) = (m1, e1) if m1 >= m2 else (m2, e2)
	if mm > m:
		m = mm
		e1, e2 = (me, i) if l[me] <= l[i] else (i, me)

p = e2
for i in range(m/2):
	p = e[p]

if m % 2 == 0:
	print p
else:
	print e[p], p
	
