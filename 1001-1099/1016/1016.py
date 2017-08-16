import sys, heapq

def id(a):
	return (int(a[1]) - 1) * 8 + ord(a[0]) - 97
def di(a):
	return '%s%d' % (chr(a%8 + 97), a/8 + 1)
def left(a):
	return (a[0], a[1], a[3], a[4], a[5], a[2])
def right(a):
	return (a[0], a[1], a[5], a[2], a[3], a[4])
def forward(a):
	return (a[2], a[4], a[1], a[3], a[0], a[5])
def backward(a):
	return (a[4], a[2], a[0], a[3], a[1], a[5])

a = sys.stdin.readline().split()
f, t = id(a[0]), id(a[1])
a = tuple([int(x) for x in a[2:]])

dist = {(f, a):a[4]}
index = {0:[(f, a, [f])]}
visit = set()
heap = [0]

while len(heap) > 0:
	min = heapq.heappop(heap)
	id, a, path = index[min].pop()
	if id == t:
		break
	visit.add((id, a))
	todo = []
	if id % 8 != 0: # left
		todo.append((id-1, left(a)))
	if id % 8 != 7: # right
		todo.append((id+1, right(a)))
	if id - 8 >= 0: #forkward
		todo.append((id-8, forward(a)))
	if id + 8 < 64: #backward
		todo.append((id+8, backward(a)))
	for idd, b in todo:
		if (idd, b) not in visit:
			d = dist[id, a] + b[4]
			if (idd, b) not in dist or dist[idd, b] > d:
				dist[idd, b] = d
			heapq.heappush(heap, d)
			if d not in index:
				index[d] = []
			index[d].append((idd, b, path + [idd]))
print dist[id, a], ' '.join([di(x) for x in path])
