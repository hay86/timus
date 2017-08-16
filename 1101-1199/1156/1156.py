import sys

n, m = [int(x) for x in sys.stdin.readline().split()]

a = [[False]*(2*n+1) for i in range(2*n+1)]
b = [True]*(2*n+1)

for i in range(m):
	j, k = [int(x) for x in sys.stdin.readline().split()]
	a[j][k] = True
	a[k][j] = True
	b[j] = False
	b[k] = False

vis = [False]*(2*n+1)

def dfs(x, s1, s2):
	vis[x] = True
	s1.add(x)
	for i in range(1, 2*n+1):
		if a[x][i] and not vis[i]:
			dfs(i, s2, s1)

ans, single = [], []

for i in range(1, 2*n+1):
	if not vis[i]:
		if b[i]:
			single.append(i)
		else:
			s1, s2 = set(), set()
			dfs(i, s1, s2)
			ans.append((s1, s2))

mindiff = sys.maxint
path = None

def search(i, p, d):
	global mindiff, path
	if i == len(ans):
		if abs(d) < mindiff:
			mindiff = abs(d)
			path = []+p
	else:
		p.append(0)
		diff = len(ans[i][0])-len(ans[i][1])
		if diff == 0:
			search(i+1, p, d)
		else:
			d += diff
			search(i+1, p, d)
			p[-1] = 1
			d -= 2*diff
			search(i+1, p, d)
		p.pop()

search(0, [], 0)

def check(s):
	for i in range(len(s)-1):
		for j in range(i+1, len(s)):
			if a[s[i]][s[j]]:
				return True
	return False

if len(single) >= mindiff:
	s1, s2 = [], []
	for i in range(len(ans)):
		s1.extend(ans[i][path[i]])
		s2.extend(ans[i][1-path[i]])
	if len(s1) > n or len(s2) > n or check(s1) or check(s2):
		print 'IMPOSSIBLE'
	else:
		for i in range(n-len(s1)):
			s1.append(single.pop())
		for i in single:
			s2.append(i)
		s1.sort()
		s2.sort()
		print ' '.join([str(x) for x in s1])
		print ' '.join([str(x) for x in s2])
else:
	print 'IMPOSSIBLE'
