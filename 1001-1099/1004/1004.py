import sys
sys.setrecursionlimit(10000)

def root(x):
	p = x
	while p != b[p]:
		p = b[p]
	b[x] = p
	return p

def dijkstra(x, y):
	dist = [sys.maxint]*(n+1)
	prev = [None]*(n+1)
	vis = [False]*(n+1)
	dist[x] = 0
	while True:
		minp, mind = -1, sys.maxint
		for i in range(1, n+1):
			if not vis[i] and dist[i] < mind:
				mind = dist[i]
				minp = i
		if minp == y:
			break
		vis[minp] = True
		for i in range(1, n+1):
			if c[minp][i] > 0 and dist[i] > mind + c[minp][i]:
				dist[i] = mind + c[minp][i]
				prev[i] = minp
	path = []
	tmp = y
	while prev[tmp] != None:
		path.append(tmp)
		tmp = prev[tmp]
	path.append(x)
	return dist[y], path

while True:
	line = sys.stdin.readline()
	if line.strip() == '-1':
		break
	n, m = [int(x) for x in line.split()]
	a = []
	for i in range(m):
		a.append([int(x) for x in sys.stdin.readline().split()])
	a.sort(key=lambda x: x[2])
	b = [x for x in range(n+1)]
	c = [[0]*(n+1) for x in range(n+1)]
	min_path = 'No solution.'
	min_dist = sys.maxint
	count, lower = 0, 0
	for x, y, z in a:
		if c[x][y] > 0:
			continue
		count += 1
		if count < 3:
			lower += z
		elif min_dist <= lower + z:
			break
		rx, ry = root(x), root(y)
		if rx == ry:
			dist, path = dijkstra(x, y)
			if dist + z < min_dist:
				min_dist = dist + z
				min_path = ' '.join([str(i) for i in path])
		else:
			b[ry] = rx
		c[x][y] = z
		c[y][x] = z
	print min_path
