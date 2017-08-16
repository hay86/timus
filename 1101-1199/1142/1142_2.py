import sys

m = [[0]*11 for i in range(11)]
m[1][1] = 1
a = [0]*11

for i in range(2, 11):
	for j in range(1, i+1):
		m[i][j] = m[i-1][j-1]*j + m[i-1][j]*j
		a[i] += m[i][j]

for line in sys.stdin:
	i = int(line)
	if i == -1:
		break
	print a[i]
