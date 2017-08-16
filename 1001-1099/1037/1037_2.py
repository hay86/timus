import sys, heapq
from collections import deque

last = 1
used = {}
unused = []
access = deque()

for line in sys.stdin.readlines():
	p = line.find('+')
	if p > 0:
		t = int(line[:p])
		
		while len(access) > 0 and access[0][0]+600 <= t:
			tt, ii = access.popleft()
			if used[ii]+600 <= t:
				heapq.heappush(unused, ii)
				
		if len(unused) == 0:
			i = last
			last += 1
		else:
			i = heapq.heappop(unused)
		used[i] = t
		access.append((t, i))
		print i
	else:
		t, i = [int(x) for x in line.split('.')]
		
		while len(access) > 0 and access[0][0]+600 <= t:
			tt, ii = access.popleft()
			if used[ii]+600 <= t:
				heapq.heappush(unused, ii)
				
		if i not in used or used[i]+600 <= t:
			print '-'
		else:
			used[i] = t
			access.append((t, i))
			print '+'