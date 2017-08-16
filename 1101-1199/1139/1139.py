import sys

n, m = [int(x)-1 for x in sys.stdin.readline().split()]

if n < m:
	n, m = m, n

def gcd(a, b):
	if a%b == 0:
		return b
	return gcd(b, a%b)

if n%m == 0:
	print n
else:
	x = gcd(n, m)
	n, m = n/x, m/x
	print x*(n+m-1)	
