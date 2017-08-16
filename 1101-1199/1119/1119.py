import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
t = (n+m)*100
d = 100*(2-2**0.5)

k = int(sys.stdin.readline())
c = []

for i in range(k):
	a, b = [int(x) for x in sys.stdin.readline().split()]
	c.append((a, b))

c.sort(key=lambda x:(x[0],x[1]))

s = 0
if len(c) > 0:
	mat = [1]*len(c)
	for i in range(1, len(c)):
		for j in range(i-1, -1, -1):
			if c[i][0] > c[j][0] and c[i][1] > c[j][1] and mat[i] <= mat[j]:
				mat[i] = mat[j] + 1
	s = max(mat)

print int(round(t-d*s))
