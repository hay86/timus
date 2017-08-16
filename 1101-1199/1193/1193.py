import sys

n = int(sys.stdin.readline())
m = []

for i in range(n):
	t1, t2, t3 = [int(x) for x in sys.stdin.readline().split()]
	m.append((t1, t2, t3))

m.sort(key=lambda x:x[0])

gap = 0
t = 0
for i in range(n):
	t1, t2, t3 = m[i]
	if t1 > t:
		t = t1
	t += t2
	if t-t3 > gap:
		gap = t-t3

print gap
