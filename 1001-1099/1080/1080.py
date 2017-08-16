import sys

def check(x, v):
	b[x] = v
	for i in range(1, n+1):
		if a[i][x]:
			if b[i] == v:
				return False
			if b[i] == -1 and not check(i, 1-v):
				return False
	return True

def next():
	for i in range(1, n+1):
		if b[i] == -1:
			return i
	return 0

n = int(sys.stdin.readline())
a = [[False for i in range(n+1)] for j in range(n+1)]
b = [-1 for i in range(n+1)]

for i in range(n):
	y =[int(x) for x in sys.stdin.readline().split()]
	for j in y[:-1]:
		a[i+1][j] = a[j][i+1] = True

x = next()
y = True
while x and y:
	y = check(x, 0)
	x = next()


if not x and y:
	print ''.join([str(x) for x in b[1:]])
else:
	print -1
