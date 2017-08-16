import sys

h, w = [int(x) for x in sys.stdin.readline().split()]

a = []
a += [[(1,0),(-1,0),(0,1),(0,-1)]]
a += [[(2,0),(-2,0),(0,2),(0,-2),(1,1),(1,-1),(-1,1),(-1,-1)]]
a += [[(3,0),(-3,0),(0,3),(0,-3),(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]]
a += [[(4,0),(-4,0),(0,4),(0,-4),(3,1),(3,-1),(-3,1),(-3,-1),(1,3),(1,-3),(-1,3),(-1,-3),(2,2),(2,-2),(-2,2),(-2,-2)]]
a += [[(5,0),(-5,0),(0,5),(0,-5),(4,1),(4,-1),(-4,1),(-4,-1),(1,4),(1,-4),(-1,4),(-1,-4),(3,2),(3,-2),(-3,2),(-3,-2),(2,3),(2,-3),(-2,3),(-2,-3)]]

dist = [[5]*w for i in range(h)]
sum = [[0]*w for i in range(h)]

m= []
for i in range(h):
	m.append([int(x) for x in sys.stdin.readline().split()])
	
for i in range(h):
	for j in range(w):
		if m[i][j] > 0:
			for k in range(5):
				for dx, dy in a[k]:
					x, y = i+dx, j+dy
					if 0 <= x < h and 0 <= y < w and m[x][y] == 0:
						if dist[x][y] > k:
							dist[x][y] = k
							sum[x][y] = m[i][j]
						elif dist[x][y] == k:
							sum[x][y] |= m[i][j]
							
for i in range(h):
	for j in range(w):
		if m[i][j] > 0:
			print -1,
		else:
			print sum[i][j],
	print 