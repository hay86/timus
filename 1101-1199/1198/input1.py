import sys

n = int(sys.stdin.readline())
m = [[False]*n for i in range(n)]
chk = []

for i in range(n):
	while True:
		y = ord(sys.stdin.read(1)) - 48
		while not 0 <= y <= 9:
			y = ord(sys.stdin.read(1)) - 48
		j = y
		y = ord(sys.stdin.read(1)) - 48
		while 0 <= y <= 9:
			j = 10*j + y
			y = ord(sys.stdin.read(1)) - 48
		if j == 0:
			break
		m[i][j-1] = True
