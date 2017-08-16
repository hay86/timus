import sys

n, a, b = [int(x) for x in sys.stdin.readline().split()]

if a < b:
	a, b = b, a
	
p, q = 1, 1
c1, c2 = 1, 1

for i in range(1, a+1):
	p *= n+i-1
	q *= i
	c1 += p/q
	if i == b:
		c2 = c1
		
print c1*c2