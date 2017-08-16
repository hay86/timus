# http://en.wikipedia.org/wiki/Jeep_problem
import sys, math

n, m = [float(x) for x in sys.stdin.readline().split()]

k = 0
while True:
	k += 1
	d = m/(2*k-1)
	if n-d > 0:
		n -= d
	else:
		break

print '%d' % math.ceil((k-1)*m+n*(2*k-1))