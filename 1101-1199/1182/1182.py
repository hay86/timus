import sys

n = int(sys.stdin.readline())

a = [[False]*(n+1) for i in range(n+1)]
b = [True]*(n+1)

for i in range(1, n+1):
	s = set([int(x) for x in sys.stdin.readline().split()])
	for j in range(1, n+1):
		if i != j and j not in s:
			a[i][j] = True
			a[j][i] = True
			b[i] = False
			b[j] = False

vis = [False]*(n+1)

def dfs(x, s1, s2):
	vis[x] = True
	s1.add(x)
	for i in range(1, n+1):
		if a[x][i] and not vis[i]:
			dfs(i, s2, s1)

ans, single = [], []

for i in range(1, n+1):
	if not vis[i]:
		if b[i]:
			single.append(i)
		else:
			s1, s2 = set(), set()
			dfs(i, s1, s2)
			if len(s1) > len(s2):
				ans.append((s1, s2))
			else:
				ans.append((s2, s1))

pkg = [len(s1)-len(s2) for s1, s2 in ans]
vol = int(sum(pkg)/2)

min = [[i]*(len(pkg)+1) for i in range(vol+1)]
bel = [[False]*(len(pkg)+1) for i in range(vol+1)]

for i in range(1, vol+1):
	for j in range(1, len(pkg)+1):
		min[i][j] = min[i][j-1]
		if pkg[j-1] > 0 and i-pkg[j-1] >=0 and min[i-pkg[j-1]][j-1] < min[i][j]:
			bel[i][j] = True
			min[i][j] = min[i-pkg[j-1]][j-1]

path = [0]*len(pkg)
i = vol
for j in range(len(pkg),0,-1):
	if bel[i][j]:
		i -= pkg[j-1]
		path[j-1] = 1

def check(s):
	for i in range(len(s)-1):
		for j in range(i+1, len(s)):
			if a[s[i]][s[j]]:
				return True
	return False

s1, s2 = [], []
for i in range(len(ans)):
	s1.extend(ans[i][path[i]])
	s2.extend(ans[i][1-path[i]])

if check(s1) or check(s2):
	print 'No solution'
else:
	if len(s1) > len(s2):
		for i in range(len(s1)-len(s2)):
			if len(single) > 0:
				s2.append(single.pop())
	elif len(s1) < len(s2):
		for i in range(len(s2)-len(s1)):
			if len(single) > 0:
				s1.append(single.pop())
	while len(single) > 0:
		if len(single) > 0:
			s1.append(single.pop())
		if len(single) > 0:
			s2.append(single.pop())
	print len(s1), ' '.join([str(x) for x in s1])
	print len(s2), ' '.join([str(x) for x in s2])
