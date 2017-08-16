import sys

d, e, f, dp, ep, h = [int(x) for x in sys.stdin.readline().split()]

x = (dp-1)^(ep-1)
y = 0
while x != 0:
	y += 1
	x = int(x/2)

if y >= d and y >= e:
	print 'YES' if 2*y <= h+d+e else 'NO'
else:
	print 'YES' if abs(d-e) <= h else 'NO'