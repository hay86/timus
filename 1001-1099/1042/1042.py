import sys

n = int(sys.stdin.readline())

l = {}
for i in range(n):
	v = [int(x) for x in sys.stdin.readline().split()]
	for vv in v:
		if vv == -1:
			continue
		if vv-1 not in l:
			l[vv-1] = set()
		l[vv-1].add(i)

t = []
for i in range(n):
	if i not in l:
		continue
	b = [0 for j in range(n)]
	for j in l[i]:
		b[j] = 1
	d = int(''.join([str(x) for x in b]), 2)
	t.append([d, 1])

if len(t) < n:
	print 'No solution'
	sys.exit()

def foo(a, b):
	if b[0] == a[0]:
		return 0
	else:
		return 1 if b[0] > a[0] else -1

t.sort(cmp=foo)

for i in range(n-1):
	for j in range(i+1, n):
		if (t[j][0] >> (n-1-i)) == 1:
			t[j][0] ^= t[i][0]
			t[j][1] ^= t[i][1]
	t.sort(cmp=foo)

for i in range(n-1, 0, -1):
	for j in range(i-1, -1, -1):
		if (t[j][0] >> (n-1-i)) % 2 == 1:
			t[j][0] ^= t[i][0]
			t[j][1] ^= t[i][1]

for i in range(len(t)):
	if t[i][1] == 1:
		print i+1,
