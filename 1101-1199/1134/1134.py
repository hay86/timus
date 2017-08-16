import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.read().split()]
a.sort()
b = [False] * (n+1)
b[0] = True
c = True

for i in range(m):
	if a[i] <= n and not b[a[i]]:
		b[a[i]] = True
	elif a[i]+1 <= n and not b[a[i]+1]:
		b[a[i]+1] = True
	else:
		c = False
		break

print 'YES' if c else 'NO'
