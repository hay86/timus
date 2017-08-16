import sys

n = int(sys.stdin.readline())
p = set()

for i in xrange(n):
	p.add(sys.stdin.readline())

m = int(sys.stdin.readline())
t = 0

for line in sys.stdin:
	if line in p:
		t += 1

print t
