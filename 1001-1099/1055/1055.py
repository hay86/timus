# Power of each prime in binomial coefficient's factorization equals to the number of borrows in the substraction n-k in base p.
# Iterate all primes less then N and count it if prime will greater then 0;

import sys, math

def E(n, m, p):
	e = 0
	while n > 0:
		a = n % p
		b = m % p
		n = n / p
		m = m / p
		if a < b:
			e += 1
			n -= 1
	return e

n, m = [int(x) for x in sys.stdin.readline().split()]
m = min(m, n-m)

x = [True for i in range(n+1)]
y = int(math.sqrt(n))

for i in range(2, y+1):
	z = int(n/i)
	for j in range(2, z+1):
		x[i*j] = False

r = 0
for i in range(2, n+1):
	if x[i]:
		e = E(n, m, i)
		if e > 0:
			r += 1
print r
