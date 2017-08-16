import sys

n = int(sys.stdin.readline())
m = [[False]*n for i in range(n)]
chk = []

lines = sys.stdin.read()
x = 0

for i in range(n):
	while True:
		y = lines[x]
		while y == ' ' or y == '\n':
			x += 1
			y = lines[x]
		j = ord(y) - 48
		x += 1
		y = lines[x]
		while y != ' ' and y != '\n':
			j = 10*j + ord(y) - 48
			x += 1
			y = lines[x]
		if j == 0:
			break
		m[i][j-1] = True
