import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[False for i in range(n+1)] for i in range(n+1)]
mask = {}

for i in range(1, n+1):
	s = int(sys.stdin.readline())
	for j in range(s):
		ip, mk = [x.split('.') for x in sys.stdin.readline().split()]
		sub = []
		for k in range(4):
			sub.append(str(int(ip[k])&int(mk[k])))
		sub = '.'.join(sub)
		if not sub in mask:
			mask[sub] = []
		for k in mask[sub]:
			graph[k][i] = True
			graph[i][k] = True
		mask[sub].append(i)

start, end = [int(x) for x in sys.stdin.readline().split()]
visit = [False for i in range(n+1)]
queue = deque([(start, [start])])
visit[start] = True

while len(queue) > 0:
	a, p = queue.popleft()
	if a == end:
		break
	for b in range(1, n+1):
		if graph[a][b] and not visit[b]:
			visit[b] = True
			queue.append((b, p + [b]))
if a == end:
	print 'Yes'
	print ' '.join([str(x) for x in p])
else:
	print 'No'
