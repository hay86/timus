import sys

m = int(sys.stdin.readline())
q = []
c = 0

for line in sys.stdin:
	n = int(line)
	if n == -1:
		break
	c += 1
	while len(q) > 0 and q[-1][0] <= n:
		q.pop()
	q.append((n, c))
	if c >= m:
		while len(q) > 0 and q[0][1] <= c-m:
			q.pop(0)
		print q[0][0]
		
