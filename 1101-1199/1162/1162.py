# Bellman Ford Algorithm
import sys

n, m, s, v = [float(x) for x in sys.stdin.readline().split()]
n, m, s, v = int(n), int(m), int(s), v*10000000000

dist = [-sys.maxint]*(n+1)
dist[s] = v
edge = []

for i in range(m):
	edge.append([float(x) for x in sys.stdin.readline().split()])
	edge[-1][3] *= 10000000000
	edge[-1][5] *= 10000000000

for i in range(n):
	for e in edge:
		a, b, rab, cab, rba, cba = e
		a, b = int(a), int(b)
		t = (dist[a]-cab)*rab 
		if t > dist[b]:
			dist[b] = t
		t = (dist[b]-cba)*rba
		if t > dist[a]:
			dist[a] = t

ans = 'NO'
for e in edge:
	a, b, rab, cab, rba, cba = e
	a, b = int(a), int(b)
	if (dist[a]-cab)*rab > dist[b]:
		ans = 'YES'
		break
	if (dist[b]-cba)*rba > dist[a]:
		ans = 'YES'
		break
print ans
