import sys
from collections import deque

n, m = [int(x) for x in sys.stdin.readline().split()]

m2s = {}
s2m = {}
for i in range(m):
	stop = [int(x) for x in sys.stdin.readline().split()]
	for j in range(1, len(stop)):
		if not i in m2s:
			m2s[i] = []
		m2s[i].append(stop[j])
		if not stop[j] in s2m:
			s2m[stop[j]] = []
		s2m[stop[j]].append(i)

gol = [0 for i in range(n+1)]
k = int(sys.stdin.readline())
sum = 0
for i in range(k):
	a, b, c = [int(x) for x in sys.stdin.readline().split()]
	sum += a
	loc = [-1 for j in range(n+1)]
	chk = [] if b not in s2m else [] + s2m[b]
	chked = set(chk)
	loc[b] = a
	money = a-4
	while len(chk) > 0 and (money >= 0 or c == 1):
		tmp = []
		for mm in chk:
			for ss in m2s[mm]:
				if loc[ss] == -1:
					loc[ss] = money if c == 0 else a
					for mmm in s2m[ss]:
						if not mmm in chked:
							chked.add(mmm)
							tmp.append(mmm)
		chk = tmp
		money -= 4

	for j in range(1, n+1):
		if loc[j] == -1:
			gol[j] = -1
		elif gol[j] != -1:
			gol[j] += loc[j]

max = -1
stop = 0
for i in range(1, n+1):
	if gol[i] > max:
		max = gol[i]
		stop = i
if stop > 0:
	print stop, sum - max 
else:
	print 0
		