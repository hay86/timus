import sys, random

n = int(sys.stdin.readline())
c = []
for i in range(n):
	c.append([int(x) for x in sys.stdin.readline().split()])

f = True
while f:
	f = False
	d = [0]*(n+1)
	s = [False]*(n+1)
	t = 0
	for i in range(1, n+1):
		a = c[i-1]
		d1, d2, d3, d4 = 0, 0, 0, 0
		for j in range(1, a[0]+1):
			if i > a[j]:
				if s[a[j]]:
					d2 += 1
					d4 = max(d4, d[a[j]]+1)
				else:
					d1 += 1
					d3 = max(d3, d[a[j]]+1)
		g = [d1 <= 1 and d3 <= 1, d2 <= 1 and d4 <= 1]
		if g[0] and g[1]:
			g[random.randint(0,1)] = False
		if g[0]:
			for j in range(1, a[0]+1):
				if i > a[j] and not s[a[j]]:
					d[i] += 1
					d[a[j]] += 1
		elif g[1]:
			t += 1
			s[i] = True
			for j in range(1, a[0]+1):
				if i > a[j] and s[a[j]]:
					d[i] += 1
					d[a[j]] += 1
		else:
			f = True
			break

if t < n-t or (t == n-t and s[1]):
	print t
	for i in range(1, n+1):
		if s[i]:
			print i,
elif t > n-t or (t == n-t and not s[1]):
	print n-t
	for i in range(1, n+1):
		if not s[i]:
			print i,
