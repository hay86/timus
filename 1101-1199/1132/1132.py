import sys

maxn = 16383
sqr, root = [], []
for i in range(1, maxn+1):
	sqr.append(i*i)
	root.append(i)

k = int(sys.stdin.readline())
for i in range(k):
	a, n = [int(x) for x in sys.stdin.readline().strip().split(' ')]
	j, maxa= 0, (n/2)**2
	while a <= maxa:
		while j < maxn and sqr[j] < a:
			j += 1
		if j < maxn and sqr[j] == a:
			break
		a += n
	if j < maxn and sqr[j] == a:
		print root[j], n-root[j]
	else:
		print 'No root'
