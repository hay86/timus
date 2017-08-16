import sys

n = int(sys.stdin.readline())
a, b, c, d = 0, 0, 10000, 0
ans = 'YES'

for i in range(n):
	a += 1
	x = sys.stdin.readline().split()
	if x[1] == '1':
		c = int(x[2])
		b += a*c
		d += c
		a = 0
		if b > 10000:
			ans = 'NO'
			break
	else:
		d += c

if ans == 'YES':
	if b+a > 10000 or d < 10000:
		ans = 'NO'

print ans
