import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
a = []

for i in range(n):
	a.append([int(x) for x in sys.stdin.readline().split()])

ans = []

def dfs(i):
	for j in range(n):
		if i != j and a[i][j] == 0:
			a[i][j] = 1
			dfs(j)
	ans.append(i)

def dfs2(i):
	stack = [(i,0)]
	while len(stack) > 0:
		i, j = stack[-1]
		while j < n:
			if i != j and a[i][j] == 0:
				a[i][j] = 1
				stack.append((j,0))
				break
			else:
				j += 1
		if j == n:
			stack.pop()
			ans.append(i)

dfs2(m-1)

for i in range(len(ans)-1, 0, -1):
	print ans[i]+1, ans[i-1]+1
