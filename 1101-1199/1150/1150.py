import sys

n = sys.stdin.readline().strip()
m = [0]*10

for i in range(len(n)):
	a = int(n[:i]) if i > 0 else 0
	b = int(n[i+1:]) if i < len(n)-1 else 0
	c = int(n[i])
	for j in range(1, 10):
		m[j] += a*10**(len(n)-1-i)
	for j in range(1, c):
		m[j] += 10**(len(n)-1-i)
	if a > 0:
		m[0] += (a-1)*10**(len(n)-1-i)
		if c > 0:
			m[0] += 10**(len(n)-1-i)
	m[c] += b+1

for i in m:
	print i
