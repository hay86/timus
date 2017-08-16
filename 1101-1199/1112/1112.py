import sys

n = int(sys.stdin.readline())
m = []

for i in range(n):
	a, b = [int(x) for x in sys.stdin.readline().split()]
	if a > b:
		a, b = b, a
	m.append((a,b))
	
m.sort(key=lambda x:x[0])
r = [m[0]]

for i in range(1, len(m)):
	if m[i][0] >= r[-1][1]:
		r.append(m[i])
	elif m[i][1] < r[-1][1]:
		r[-1] = m[i]
		
print len(r)
for a, b in r:
	print a, b
	