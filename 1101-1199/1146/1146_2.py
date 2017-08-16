import sys
from operator import sub

n = int(sys.stdin.readline())
x = [[0]*n for i in range(n)]
i = 0

for line in sys.stdin:
	y = line.split()
	sum = 0
	for j in range(n):
		sum += int(y[j])
		x[j][i] = sum
	i += 1
	
def max_sum(arr):
	max1, max2 = -sys.maxint, 0
	for a in arr:
		max2 += a
		if max2 > max1:
			max1 = max2
		if max2 < 0:
			max2 = 0
	return max1
	
max = -sys.maxint

for y in x:
	m = max_sum(y)
	if m > max:
		max = m

for i in range(1,n):
	for j in range(i):
		m = max_sum(map(sub, x[i], x[j]))
		if m > max:
			max = m
			
print max
		