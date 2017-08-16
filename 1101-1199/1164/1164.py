import sys

n, m, p = [int(x) for x in sys.stdin.readline().split()]
c = [0]*26
s = ord('A')

for i in range(n):
	line = sys.stdin.readline()
	for j in range(m):
		c[ord(line[j])-s] += 1

for i in range(p):
	line = sys.stdin.readline().strip()
	for j in range(len(line)):
		c[ord(line[j])-s] -= 1

for i in range(26):
	for j in range(c[i]):
		sys.stdout.write(chr(s+i))
