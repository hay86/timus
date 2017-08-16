import sys

n, m, p = [int(x) for x in sys.stdin.readline().split()]
chs = sys.stdin.readline().strip()

c, y, x = set(), set(), set()

for stop in sys.stdin:
	stop = stop.strip()
	flag = True
	for xx in list(x):
		if xx in stop:
			flag = False
			break
		elif stop in xx:
			x.remove(xx)
	if flag:
		x.add(stop)

for stop in x:
	if len(stop) > 2:
		for i in range(2, len(stop)):
			y.add(stop[:i])

for ch in chs:
	if ch not in x:
		c.add(ch)

s1 = {'' : 1}

for i in range(m):
	s2 = {}
	for pfx, cnt in s1.items():
		for ch in c:
			pfxch = pfx + ch
			key = None
			flag = True
			for j in range(len(pfxch)-1):
				ppfxch = pfxch[j:]
				if ppfxch in x:
					flag = False
					break
				elif key is None and ppfxch in y:
					key = ppfxch
			if flag:
				if key is None:
					key = ch
				if key not in s2:
					s2[key] = cnt
				else:
					s2[key] += cnt
	s1 = s2

print sum(s2.values())
