import sys
from collections import Counter

n = int(sys.stdin.readline())
a = sys.stdin.readline().strip()
b = [(a[i], i+1) for i in range(len(a))]
c = Counter(a)

def neq(x, y, z):
	return x != y and y != z and x != z

print n-3

for i in range(n-3):
	for j in range(len(b)-1, -1, -1):
		if neq(b[j][0], b[j-1][0], b[j-2][0]) and c[b[j-1][0]] > 1:
			break
	print b[j-2][1], b[j][1]
	c[b[j-1][0]] -= 1
	b.pop(j-1)
			