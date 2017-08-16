import sys, heapq

seq = [int(x) for x in sys.stdin.readline().split()]
map = {}
ava = []

for i in seq:
	if not i in map:
		map[i] = 1
	else:
		map[i] += 1

for i in range(1, len(seq)+2):
	if not i in map:
		heapq.heappush(ava, i)

edge = {}
		
for a in seq:
	b = heapq.heappop(ava)
	if not a in edge:
		edge[a] = []
	if not b in edge:
		edge[b] = []
	edge[a].append(b)
	edge[b].append(a)
	map[a] -= 1
	if map[a] == 0:
		heapq.heappush(ava, a)

key = edge.keys()
key.sort()
for k in key:
	val = edge[k]
	val.sort()
	print '%d:' % k,
	for v in val:
		print v,
	print
	