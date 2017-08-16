import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
g = [[False for i in range(n+1)] for i in range(n+1)]
v = set()

for i in range(m):
	a, b = [int(x) for x in sys.stdin.readline().split()]
	g[a][b] = True
	g[b][a] = True
	v.add(a)
	v.add(b)

ans = []

while len(v) > 0:
	stack = [v.pop()]
	visit = set()
	edges = {}
	
	while len(stack) > 0:
		j = stack.pop()
		if not j in visit:
			visit.add(j)
			for i in range(n, 0, -1):
				if g[j][i] and not i in visit and not i in stack:
					edges[i] = (j, i)
					stack.append(i)
	v.difference_update(visit)
	
	edge_set = set(edges.values())
	vert_arr = list(visit)
	vert_arr.sort()
	for a in range(len(vert_arr)-1):
		for b in range(a+1, len(vert_arr)):
			x, y = vert_arr[a], vert_arr[b]
			if g[x][y] and not (x, y) in edge_set and not (y, x) in edge_set:
				p1 = [x]
				while x in edges:
					x, t = edges[x]
					p1.insert(0, x)
				p2 = [y]
				while y in edges:
					y, t = edges[y]
					p2.insert(0, y)
				for i in range(min(len(p1), len(p2))):
					if p1[i] != p2[i]:
						break
				t = p1[:i-1:-1] + [p1[i-1]] + p2[i:]
				ans.append('%d ' % len(t) + ' '.join([str(tt) for tt in t]))
					
print len(ans)
for p in ans:
	print p
	
	