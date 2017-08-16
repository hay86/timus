import sys

n = int(sys.stdin.readline())

for line in sys.stdin:
	a = list(line.strip())
	b = len(a)
	c = d = 0
	for i in range(b):
		if a[i] == '1':
			c += i+1

	if b == n-1:
		for i in range(b, -1, -1):
			if i < b and a[i] == '1':
				d += 1
			if (c+d) % (n+1) == 0:
				a.insert(i, '0')
				break
			if (c+d+i+1) % (n+1) == 0:
				a.insert(i, '1')
				break
	if b == n:
		for i in range(b-1, -1, -1):
			if a[i] == '1' and (c-i-1) % (n+1) == 0:
				a[i] = '0'
				break
	if b == n+1:
		for i in range(b-1, -1, -1):
			if a[i] == '1':
				d += 1
			if a[i] == '0' and (c-d) % (n+1) == 0:
				a.pop(i)
				break
			if a[i] == '1' and (c-d-i) % (n+1) == 0:
				a.pop(i)
				break
	print ''.join(a)
