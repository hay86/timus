import sys, heapq

def alloc(i, t):
	if t not in desu:
		heapq.heappush(access, t)
		desu[t] = set()
	desu[t].add(i)
	used[i] = t
def delloc(i):
	if used[i] in desu:
		desu[used[i]].remove(i)
def gc(t):
	while len(access) > 0 and access[0]+600 <= t:
		min_t = heapq.heappop(access)
		if min_t in desu:
			for i in desu[min_t]:
				heapq.heappush(unused, i)
			desu.pop(min_t)
	
last = 1
used = {}
unused = []
desu = {}
access = []

for line in sys.stdin.readlines():
	p = line.find('+')
	if p > 0:
		t = int(line[:p])
		gc(t)
		if len(unused) == 0:
			i = last
			last += 1
		else:
			i = heapq.heappop(unused)
		alloc(i, t)
		print i
	else:
		t, i = [int(x) for x in line.split('.')]
		if i not in used:
			print '-'
		elif used[i]+600 <= t:
			delloc(i)
			heapq.heappush(unused, i)
			print '-'
		else:
			delloc(i)
			alloc(i, t)
			print '+'