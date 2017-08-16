import sys

n = int(sys.stdin.readline())
m = [[False]*n for i in range(n)]
chk = []

i = 0
for line in sys.stdin:
		y = [int(x) for x in line.split()]
		for j in y[:-1]:
			m[i][j-1] = True
		i += 1
