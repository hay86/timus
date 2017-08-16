import sys

n = int(sys.stdin.readline())
m = [[False]*n for i in range(n)]

for i in range(n):
	y = [int(x) for x in sys.stdin.readline().split()]
	for j in y[:-1]:
		m[i][j-1] = True

for k in range(n):
	for i in range(n):
		for j in range(n):
			if not m[i][j] and m[i][k] and m[k][j]:
				m[i][j] = True

for i in range(n):
	flag = True
	for j in range(n):
		if i != j and not m[i][j]:
			flag = False
			break
	if flag:
		print i+1,
print 0
			
