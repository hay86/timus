import sys

n = int(sys.stdin.readline())
m = []

for line in sys.stdin:
	m.append([int(x) for x in line.split()])

max3 = -sys.maxint

for i in range(n):
	max2 = [0]*(i+1)
	for j in range(n):
		sum = 0
		for k in range(i+1):
			sum += m[i-k][j]
			tmp = sum + max2[k]
			max2[k] = max(tmp, 0)
			if tmp > max3:
				max3 = tmp

print max3
