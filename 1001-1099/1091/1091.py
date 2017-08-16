import sys

k, s = [int(x) for x in sys.stdin.readline().split()]

def C(n, m):
	a = max(m, n-m)
	b = min(m, n-m)
	r = 1
	for i in range(a+1, n+1):
		r *= i
	for i in range(2, b+1):
		r /= i
	return r

prime = [2,3,5,7,11,13,17,19,23,29]
c = 0
for div in range(2, int(s/k)+1):
	if not div in prime:
		continue
	for p in prime:
		if p == div:
			break
		if int(s/(div*p)) >= k:
			c -= C(int(s/(div*p)), k)
	c += C(int(s/div), k)
	if c >= 10000:
		c = 10000
		break
	
print c