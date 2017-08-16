import sys

n, m = [int(x) for x in sys.stdin.readline().split()]

e = [[False for i in range(n+1)] for i in range(m+1)]
for line in sys.stdin.readlines():
	a, b = [int(x) for x in line.split()]
	e[a][b] = True

def dfs(x):
	for y in range(1, m+1):
		if e[x][y] and not visit[y]:
			visit[y] = True
			if match[y] == 0 or dfs(match[y]):
				match[y] = x
				return True
	return False

match = [0 for i in range(m+1)]
total = 0

for i in range(1, n+1):
	visit = [False for j in range(m+1)]
	if dfs(i):
		total += 1

print total
for i in range(1, m+1):
	if match[i] != 0:
		print i, match[i]
