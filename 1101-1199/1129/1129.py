import sys, random
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
g = [[False]*n for i in range(n)]
d = [0]*n
g_y = [0]*n

for i in range(n):
	e = [int(x)-1 for x in sys.stdin.readline().split()]
	d[i] = e[0]+1
	for j in e[1:]:
		g[i][j] = True
		g[j][i] = True

def dfs(i):
	for j in range(n):
		if g[i][j] == True:
			g[i][j] = False
			g[j][i] = False
			d[i] -= 1
			d[j] -= 1
			if dfs(j):
				break
	path.append(i)
	return True

while True:
	k = -1
	for i in range(n):
		if d[i] > 0:
			k = i if k == -1 or d[i]%2 == 1 else k
			if d[i]%2 == 1:
				break
	if k == -1:
		break
	path = []
	dfs(k)
	path.reverse()
	for i in range(1, len(path)):
		a, b = path[i-1], path[i]
		if g_y[a] < 1 and g_y[b] > -1:
			g[a][b] = 'G'
			g[b][a] = 'Y'
			g_y[a] += 1
			g_y[b] -= 1
		elif g_y[a] > -1 and g_y[b] < 1:
			g[a][b] = 'Y'
			g[b][a] = 'G'
			g_y[a] -= 1
			g_y[b] += 1
		else:
			x = 0/0

for i in range(n):
	for j in range(n):
		if g[i][j] != False:
			print g[i][j],
	print
