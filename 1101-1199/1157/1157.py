import sys

c = [1] * 10001

for i in range(2, 101):
	for j in range(i, 10000/i+1):
		c[i*j] += 1

m, n, k = [int(x) for x in sys.stdin.readline().split()]

success = False
for i in range(1, 10001-k):
	if c[i] == m and c[i+k] == n:
		print i+k
		success = True
		break
if not success:
	print 0
