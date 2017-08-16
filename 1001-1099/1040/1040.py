import sys
sys.setrecursionlimit(10000)

n, m = [int(x) for x in sys.stdin.readline().split()]

edge = {}
input = []

for i in range(m):
	a, b = [int(x) for x in sys.stdin.readline().split()]
	input.append((a, b))
	if a not in edge:
		edge[a] = []
	if b not in edge:
		edge[b] = []
	edge[a].append(b)
	edge[b].append(a)


visit = [False for i in range(n+1)]

def next():
	items = edge.items()
	for x, y in items:
		if not visit[x] and len(y) == 1:
			return x
	for x, y in items:
		if not visit[x] and len(y) > 2:
			return x
	for x, y in items:
		if not visit[x]:
			return x
	return None

def dfs(a, z):
	visit[a] = True
	path = []
	flag = False
	for b in edge[a]:
		if not visit[b]:
			path.append((a, b))
			path.extend(dfs(b, a))
			flag = True
	if not flag:
		for b in edge[a]:
			if b != z:
				path.append((a, b))
				break
	return path

e = []
a = next()

while a != None:
	if len(edge[a]) == 2:
		e = dfs(a, None) + e
	else:
		e.extend(dfs(a, None))
	a = next()

ids = {}
for i in range(len(e)):
	ids[e[i]] = i+1

id = len(e)+1
print 'YES'
for a, b in input:
	if (a, b) in ids:
		print ids[(a, b)],
	elif (b, a) in ids:
		print ids[(b, a)],
	else:
		print id,
		id += 1

