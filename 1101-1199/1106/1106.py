import sys

n = int(sys.stdin.readline())
m = [False] * (n+1)
a = []

for i in range(1, n+1):
	line = sys.stdin.readline()
	if not m[i]:
		a.append(i)
		m[i] = True
		b = [int(x) for x in line.split()]
		for j in b:
			m[j] = True

print len(a)
if len(a) > 0:
	for x in a:
		print x,
