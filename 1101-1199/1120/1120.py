import sys

n = int(sys.stdin.readline())
n *= 2
m = int(n**0.5)

for i in range(m, -1, -1):
	if n%i == 0:
		j = n/i-i+1
		if j%2 == 0:
			print j/2, i
			break
