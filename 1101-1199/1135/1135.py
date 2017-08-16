import sys

n = int(sys.stdin.readline())

s, e = 0, 0
t = 0

for line in sys.stdin:
	for ch in line:
		if ch == '<':
			t += e-s
			s += 1
			e += 1
		elif ch == '>':
			e += 1

print t
