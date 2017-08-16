import sys, random

n = int(sys.stdin.readline())
g = [[False for i in range(2*n+1)] for i in range(2*n+1)]
p = 0

for i in range(2*n+1):
	line = sys.stdin.readline()
	for j in range(2*n+1):
		if line[j] == '+':
			g[i][j] = True
			p += 1
	
def dfs(j):
	for i in seq:
		if g[i][j] and not visit[i]:
			visit[i] = True
			if match[i] == -1 or dfs(match[i]):
				match[i] = j
				used[j] = True
				return True
	return False
	
def count():
	c = 0
	for i in range(2*n+1):
		for j in range(2*n+1):
			if g[i][j]:
				c += 1
	return c

result = []
seq = range(2*n+1)

while p > 2*n:
	m = 0
	match = [-1 for i in range(2*n+1)]
	used = [False for i in range(2*n+1)]
	random.shuffle(seq)
	for j in seq:
		visit = [False for i in range(2*n+1)]
		if dfs(j):
			m += 1
	j = 0
	for i in seq:
		if match[i] == -1:
			while j<2*n+1 and used[j]:
				j += 1
			match[i] = j
			used[j] = True
		g[i][match[i]] = not g[i][match[i]]
	result.append(match)
	p = count()
	
print 'There is solution:'
for r in result:
	print ' '.join([str(x+1) for x in r])