import sys
	
n = int(sys.stdin.readline())
m = []
for i in range(n):
	x, y = [int(x) for x in sys.stdin.readline().split()]
	m.append((x, y, i+1))

m = sorted(m, key=lambda x: x[0], reverse=True)
r = []
g_idx = -1
g_max = 1
for mm in m:
	idx = -1
	max = 1
	for i in range(len(r)):
		if r[i][-1][0] != mm[0] and r[i][-1][1] < mm[1] and max < len(r[i]) + 1:
			max = len(r[i]) + 1
			idx = i
	if idx == -1:
		r.append([mm])
	else:
		r.append([]+r[idx])
		r[-1].append(mm)
	if g_max < len(r[-1]):
		g_max = len(r[-1])
		g_idx = len(r)-1
		
print len(r[g_idx])
print ' '.join([str(x) for x in [y[2] for y in r[g_idx]]])
	

