import sys

n = int(sys.stdin.readline())

m = n%3
if m == 0:
	print 2
else:
	print 1
	print m
