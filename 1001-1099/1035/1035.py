import sys, time

n, m = [int(x) for x in sys.stdin.readline().split()]
size = (n+1)*(m+1)

degree = [0 for i in range(size)]
father = [i for i in range(size)]
rank = [0 for i in range(size)]
thread = [-1 for i in range(size)]

def root(x):
	if father[x] == x:
		return x
	else:
		father[x] = root(father[x])
		return father[x]

def update_union(a, b):
	x = root(a)
	y = root(b)
	if rank[x] > rank[y]:
		father[y] = x
	else:
		father[x] = y
		if rank[x] == rank[y]:
			rank[y] += 1

def update_degree(a, b, inc):
	degree[a] += inc
	degree[b] += inc

def id(i, j):
	return i*(m+1)+j;

for i in range(n):
	d = sys.stdin.readline().strip()
	for j in range(m):
		if d[j] == '\\' or d[j] == 'X':
			a, b = id(i, j), id(i+1, j+1)
			update_degree(a, b, 1)
			update_union(a, b)
		if d[j] == '/' or d[j] == 'X':
			a, b = id(i+1, j), id(i, j+1)
			update_degree(a, b, 1)
			update_union(a, b)
			
for i in range(n):
	d = sys.stdin.readline().strip()
	for j in range(m):
		if d[j] == '\\' or d[j] == 'X':
			a, b = id(i, j), id(i+1, j+1)
			update_degree(a, b, -1)
			update_union(a, b)
		if d[j] == '/' or d[j] == 'X':
			a, b = id(i+1, j), id(i, j+1)
			update_degree(a, b, -1)
			update_union(a, b)

for i in range(len(father)):
	j = root(i)
	if i != j:
		if thread[j] == -1:
			thread[j] = abs(degree[j])
		thread[j] += abs(degree[i])

total = 0
for i in range(len(thread)):
	if thread[i] == 0:
		total += 1
	elif thread[i] > 0:
		total += thread[i]/2
print total
