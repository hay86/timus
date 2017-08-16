import sys
sys.setrecursionlimit(10000)

k = int(sys.stdin.readline())

prime = [True for i in range(10667)]
prime[0], prime[1], prime[2] = False, False, False

for i in range(2, 104):
	j = 2*i
	while j < 10667:
		if prime[j]:
			prime[j] = False
		j += i

def egcd(a, b):
	if b == 0:
		return (a, 1, 0)
	else:
		r, x, y = egcd(b, a%b)
		x, y = y, x - a/b * y
		return (r, x, y)

def mod(a, n, b):
	if n == 0:
		return 1
	elif n == 1:
		return a % b
	else:
		r = mod(a, n/2, b)
		r = (r*r) % b if n % 2 == 0 else (r*r*a) % b
		return r

for i in range(k):
	e, n, c = [int(x) for x in sys.stdin.readline().split()]
	m = int(n**0.5) + 1
	
	for p in range(3, m):
		if prime[p] and n % p == 0:
			q = n / p
			r = (p-1) * (q-1)
			if prime[q] and e < r:
				gcd, x, y = egcd(r, e)
				if gcd == 1:
					d = y % r
					print mod(c, d, n)
					break

