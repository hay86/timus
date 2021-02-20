import sys, heapq
from collections import deque

last = 1
used = [-1]*30001
unused = []
access = deque()

for line in sys.stdin:
	p = [x for x in line.strip().split()]
	t = int(p[0])

	while len(access) > 0 and access[0][0] + 600 <= t:
		tt, ii = access.popleft()
		if used[ii] + 600 <= t:
			heapq.heappush(unused, ii)

	if p[1] == '+':
		if len(unused) == 0:
			i = last
			last += 1
		else:
			i = heapq.heappop(unused)
		used[i] = t
		access.append((t, i))
		print(i)

	elif p[1] == '.':
		i = int(p[2])
		if used[i] < 0 or used[i] + 600 <= t:
			print('-')
		else:
			used[i] = t
			access.append((t, i))
			print('+')