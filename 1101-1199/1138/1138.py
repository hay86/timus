import sys

n, s = [int(x) for x in sys.stdin.readline().split()]
a = [0]*(n+1)
a[s] = 1

for i in range(s+1, n+1):
	for j in range(101, 201):
		k = i*100
		if k%j == 0:
			k /= j
			if a[k] != 0 and a[k]+1 > a[i]:
				a[i] = a[k]+1
					
print max(a)