import sys

n, k = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.read().split()]
m = 1
q = []
w, b = 0, 0
for i in range(n):
	if a[i] == 0:
		w += 1
		if i>0 and a[i-1] == 1:
			m += 1
	else:
		b += 1
		if i>0 and a[i-1] == 0:
			m += 1
	q.append(w*b)

if k >= m:
	print 0
else:
	m = [[0]*n for i in range(n)]
	for i in range(n):
		w, b = 0, 0
		for j in range(i, n):
			if a[j] == 0:
				w += 1
			else:
				b += 1
			m[i][j] = w*b
	
	for i in range(1, k):
		p = [sys.maxint]*n
		for j in range(i, n):
			for l in range(j, i-1, -1):
				h = q[l-1] + m[l][j]
				if h < p[j]:
					p[j] = h
		q = p
	print q[n-1]
