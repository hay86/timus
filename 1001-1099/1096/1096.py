import sys

k = int(sys.stdin.readline())
e = {}

for i in range(1, k+1):
	a, b = [int(x) for x in sys.stdin.readline().split()]
	if not a in e:
		e[a] = []
	e[a].append((b,i))

x = [int(x) for x in sys.stdin.readline().split()]
chk = [(y, []) for y in x[1:]]
chked = set(x[1:])

m = 0
ans = None

while len(chk) > 0:
	tmp = []
	for c, p in chk:
		if c in e:
			for ee, rr in e[c]:
				if ee not in chked:
					pp = p + [rr]
					if ee == x[0]:
						ans = pp
						break
					chked.add(ee)
					tmp.append((ee, pp))
	chk = tmp
	m += 1
	if ans != None:
		break
	
if ans == None:
	print 'IMPOSSIBLE'
else:
	print m
	for a in ans:
		print a