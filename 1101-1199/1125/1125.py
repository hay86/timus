import sys

m, n = [int(x) for x in sys.stdin.readline().split()]
a0 = []
a1 = []
b = [False]*m
c = [False]*n
d = []

for i in range(1,m+1):
	for j in range(1,n+1):
		k = (i**2+j**2)**0.5
		if k == int(k):
			d.append((i,j))

for i in range(m):
	a0.append([x=='W' for x in list(sys.stdin.readline().strip())])
for i in range(m):
	a1.append([int(x) for x in sys.stdin.readline().split()])

for i in range(m):
	for j in range(n):
		if a1[i][j]%2 == 1:
			b[i] = not b[i]
			c[j] = not c[j]
			a0[i][j] = not a0[i][j]
			for p, q in d:
				if i+p < m and j+q < n:
					a0[i+p][j+q] = not a0[i+p][j+q]
				if i+p < m and j-q > -1:
					a0[i+p][j-q] = not a0[i+p][j-q]
				if i-p > -1 and j+q < n:
					a0[i-p][j+q] = not a0[i-p][j+q]
				if i-p > -1 and j-q > -1:
					a0[i-p][j-q] = not a0[i-p][j-q]

for i in range(m):
	for j in range(n):
		if b[i] ^ c[j]:
			sys.stdout.write('B' if a0[i][j] else 'W')
		else:
			sys.stdout.write('W' if a0[i][j] else 'B')
	print 
