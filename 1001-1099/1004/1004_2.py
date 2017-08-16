import sys

while True:
	line = sys.stdin.readline()
	if line.strip() == '-1':
		break
	n, m = [int(x) for x in line.split()]

	g = [[sys.maxint for x in range(n+1)] for y in range(n+1)]
	d = [[sys.maxint for x in range(n+1)] for y in range(n+1)]
	p = [[[] for x in range(n+1)] for y in range(n+1)]
	for i in range(1, m+1):
		f, t, l = [int(x) for x in sys.stdin.readline().split()]
		d[f][t] = d[t][f] = g[f][t] = g[t][f] = min(g[f][t], l)
		p[f][t] = [f, t]
		p[t][f] = [t, f]

	min_dist = sys.maxint
	min_path = 'No solution.'
	for k in range(1, n+1):
		for i in range(1, k):
			for j in range(1, i):
				tmp = g[i][j] + d[i][k] + d[j][k]
				if tmp < min_dist:
					min_dist = tmp
					min_path = ' '.join([str(x) for x in p[i][j] + [k]])
		for i in range(1, n+1):
			for j in range(1, i):
				tmp = g[i][k] + g[k][j]
				if tmp < g[i][j]:
					p[i][j] = p[i][k] + p[k][j][1:]
					p[j][i] = p[i][j][::-1]
					g[i][j] = g[j][i] = tmp

	print min_path
