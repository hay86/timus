import sys

n = int(sys.stdin.readline())
m = []

for line in sys.stdin:
	m.append(int(line))

m.sort()
for i in range(n-2, -1, -1):
	m[i] = 2*(m[i]*m[i+1])**0.5

print '%.2f' % m[0]
