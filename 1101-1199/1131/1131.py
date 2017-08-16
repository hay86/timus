import sys, math

n, k = [int(x) for x in sys.stdin.readline().split()]
a, b = 1, 0

while a < n and a <= k:
	a *= 2
	b += 1

if a < n:
	if (n-a)%k == 0:
		b += (n-a)/k
	else:
		m = (n-a)%k
		b += (n-a-m)/k + 1

print b
