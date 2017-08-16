import sys

def nextint():
	buff = []
	ch = sys.stdin.read(1)
	while ord(ch) < ord('0') or ord(ch) > ord('9'):
		ch = sys.stdin.read(1)
	while ord('0') <= ord(ch) <= ord('9'):
		buff.append(ch)
		ch = sys.stdin.read(1)
	return int(''.join(buff))

n = nextint()
m, di, do = {}, {}, {}

for i in range(n):
	stop = nextint()
	a = nextint()
	for j in range(stop):
		b = nextint()
		if a not in m:
			m[a] = set()
		m[a].add(b)
		if a not in do:
			do[a] = 1
		else:
			do[a] += 1
		if b not in di:
			di[b] = 1
		else:
			di[b] += 1
		a = b

visit = []

def dfs(i):
	if do[i] == 0:
		visit.append(i)
	else:
		l = list(m[i])
		for j in l:
			if j in m[i]:
				m[i].remove(j)
				do[i] -= 1
				di[j] -= 1
				dfs(j)
		visit.append(i)

dfs(a)

print len(visit)-1,
for i in range(-1, -len(visit)-1, -1):
	print visit[i],
