import sys

n = int(sys.stdin.readline())
m = [[] for i in range(101)]

for line in sys.stdin.readlines():
	i = line.find(' ')
	a = int(line[:i])
	b = int(line[i+1:])
	m[b].append(a)

for i in range(100, -1, -1):
	for j in m[i]:
		print j, i
