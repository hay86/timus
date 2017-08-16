import sys

n = int(sys.stdin.readline())
m = []

for i in range(n):
	x, y = [int(j) for j in sys.stdin.readline().split()]
	m.append((x, y, i+1))

m.sort(key=lambda x:(x[0],x[1]))

for i in range(n/2):
	print m[2*i][2], m[2*i+1][2]
