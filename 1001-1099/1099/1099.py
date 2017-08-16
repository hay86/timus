import sys
from collections import deque

n = int(sys.stdin.readline())
m = [[False for i in range(n+1)] for i in range(n+1)]
match = [-1 for i in range(n+1)]

for line in sys.stdin.readlines():
	a, b = [int(x) for x in line.split()]
	m[a][b] = True
	m[b][a] = True
	if match[a] == -1 and match[b] == -1:
		match[a] = b
		match[b] = a

def ancestor(u, v):
	inpath = [False for i in range(n+1)]
	while True:
		u = root[u]
		inpath[u] = True
		if match[u] == -1:
			break
		u = prev[match[u]]
	while True:
		v = root[v]
		if inpath[v]:
			return v
		v = prev[match[v]]

def reset(u, a, inflower):
	while u != a:
		v = match[u]
		inflower[root[u]] = True
		inflower[root[v]] = True
		v = prev[v]
		if root[v] != a:
			prev[v] = match[u]
		u = v

def contract(u, v):
	a = ancestor(u, v)
	inflower = [False for i in range(n+1)]
	reset(u, a, inflower)
	reset(v, a, inflower)
	if root[u] != a:
		prev[u] = v
	if root[v] != a:
		prev[v] = u
	for i in range(1, n+1):
		if inflower[root[i]]:
			root[i] = a
			if not inque[i]:
				que.append(i)
				inque[i] = True

for i in range(1, n+1):
	if match[i] != -1:
		continue
	prev = [-1 for j in range(n+1)]
	inque = [False for j in range(n+1)]
	root = [j for j in range(n+1)]

	que = deque([i])
	inque[i] = True
	done = False

	while len(que) > 0 and not done:
		u = que.popleft()
		for v in range(1, n+1):
			if not m[u][v] or root[u] == root[v] or match[u] == v:
				continue
			if v == i or (match[v] != -1 and prev[match[v]] != -1):
				contract(u, v)
			elif prev[v] == -1:
				prev[v] = u
				if match[v] != -1:
					que.append(match[v])
					inque[match[v]] = True
				else:
					u = v
					while u != -1:
						v = prev[u]
						w = match[v]
						match[u] = v
						match[v] = u
						u = w
					done = True
					break

count = 0
for i in range(1, n+1):
	count += 1 if match[i] != -1 else 0
print count
for i in range(1, n+1):
	if i < match[i]:
		print i, match[i]