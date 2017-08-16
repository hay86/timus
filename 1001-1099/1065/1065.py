import sys

n, m = [int(x) for x in sys.stdin.readline().split()]

tower = []
for i in range(n):
	x, y = [int(j) for j in sys.stdin.readline().split()]
	tower.append((x, y))

monument = []
for i in range(m):
	x, y = [int(j) for j in sys.stdin.readline().split()]
	monument.append((x, y))

dist = [[0 for i in range(n)] for i in range(n)]
cos = [[-2 for i in range(n)] for i in range(n)]
for i in range(n):
	for j in range(n):
		if i == j:
			continue
		x0, y0 = tower[i]
		x1, y1 = tower[j]
		v1 = ((x1-x0), (y1-y0))
		if dist[i][j] == 0:
			dist[i][j] = (v1[0]**2 + v1[1]**2) **0.5
		x2, y2 = tower[(i+1)%n]
		v2 = ((x2-x0), (y2-y0))
		if dist[i][(i+1)%n] == 0:
			dist[i][(i+1)%n] = (v2[0]**2 + v2[1]**2) **0.5
		cos[i][j] = (v1[0]*v2[0] + v1[1]*v2[1]) / (dist[i][(i+1)%n] * dist[i][j])
		
cos2 = [-2 for i in range(n)]
for i in range(n):
	for j in range(m):
		x0, y0 = tower[i]
		x1, y1 = tower[(i+1)%n]
		v1 = ((x1-x0), (y1-y0))
		x2, y2 = monument[j]
		v2 = ((x2-x0), (y2-y0))
		d = (v2[0]**2 + v2[1]**2) **0.5
		k = (v1[0]*v2[0] + v1[1]*v2[1]) / (dist[i][(i+1)%n] * d)
		if k > cos2[i]:
			cos2[i] = k

save = [[-1 for i in range(n)] for i in range(n)]
for i in range(n):
	total = 0
	k = (i+n-1)%n
	for j in range(1, n):
		k1 = (i+j-1)%n
		k2 = (i+j)%n
		total += dist[k1][k2]
		if cos[i][k] < cos[i][k2] > cos2[i]:
			save[i][k2] = total - dist[i][k2]
		else:
			break

maxsave = 0
for k in range(n):
	for i in range(n):
		for j in range(i+2, i+n):
			jj = j%n
			if i < jj < k or k < i < jj or jj < k < i:
				if save[jj][k] != -1 and save[k][i] != -1 and save[i][jj] != -1:
					maxsave = max(maxsave, save[jj][k] + save[k][i] + save[i][jj])
	for i in range(n):
		for j in range(i+2, i+n):
			jj = j%n
			if i < k < jj or k < jj < i or jj < i < k:
				if save[i][k] != -1 and save[k][jj] != -1 and save[i][jj] < save[i][k] + save[k][jj]:
					save[i][jj] = save[i][k] + save[k][jj]

total = 0
for i in range(n):
	total += dist[i][(i+1)%n]
print '%.2f' % round(total-maxsave, 2)
