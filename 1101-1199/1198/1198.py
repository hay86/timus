import sys
from collections import deque

sys.setrecursionlimit(2000)

n = int(sys.stdin.readline())
m = [[False]*n for i in range(n)]

for i in range(n):
	y = [int(x) for x in sys.stdin.readline().split()]
	for j in y[:-1]:
		m[i][j-1] = True

def dfs(i, visit):
	visit[i] = True
	v[i] = True
	for j in range(n):
		if m[i][j] and not visit[j]:
			visit = dfs(j, visit)
	return visit

def rdfs(i, visit):
	visit[i] = True
	for j in range(n):
		if m[j][i] and not visit[j]:
			visit = rdfs(j, visit)
	return visit

def rdfs_once(i):
	v[i] = True
	for j in range(n):
		if m[j][i] and not v[j]:
			return rdfs_once(j)
	return i

v = [False] * n

while True:
	start = None
	for i in range(n):
		if not v[i]:
			start = i
			break
	if start is None:
		break
	
	root = rdfs_once(start)
	visit = dfs(root, [False] * n)
	dangerous = True
	
	for i in range(n):
		if not visit[i]:
			dangerous = False
			break
	
	if dangerous:
		break

if not dangerous:
	sys.stdout.write('0\n')
else:
	visit = rdfs(root, [False] * n)
	for i in range(n):
		if visit[i]:
			sys.stdout.write('%d ' % (i+1))
	sys.stdout.write('0\n')
