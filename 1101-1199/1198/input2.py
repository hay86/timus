import sys

n = int(sys.stdin.readline())
m = [[False]*n for i in range(n)]
chk = []

for i in range(n):
		y = [int(x) for x in sys.stdin.readline().split()]
		for j in y[:-1]:
			m[i][j-1] = True
