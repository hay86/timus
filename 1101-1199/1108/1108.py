# http://oeis.org/A000058
import sys
 
n = int(sys.stdin.readline())
a = 2
for i in range(n):
	print a
	if i == n-1:
		break
	a = a**2 -a +1