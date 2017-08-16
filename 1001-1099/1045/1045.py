import sys
sys.setrecursionlimit(10000)

n, k = [int(x) for x in sys.stdin.readline().split()]
g = {}

for i in range(n-1):
	a, b = [int(x) for x in sys.stdin.readline().split()]
	if not a in g:
		g[a] = []
	if not b in g:
		g[b] = []
	g[a].append(b)
	g[b].append(a)

def win(k, b):
	for c in g[b]:
		if c == k:
			continue
		if win(b, c):
			return False
	return True

ans = n+1
if k in g:
	for b in g[k]:
		if win(k, b) and ans > b:
			ans = b

if ans <= n:
	print 'First player wins flying to airport %d' % ans
else:
	print 'First player loses'
