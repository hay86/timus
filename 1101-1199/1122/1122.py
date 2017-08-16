import sys
from collections import deque

a = []
for i in range(4):
	a.extend(['0' if x=='W' else '1' for x in list(sys.stdin.readline().strip())])
a = int(''.join(a), 2)

b = []
for i in range(3):
	b.extend([x=='1' for x in list(sys.stdin.readline().strip())])

c = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
d=[]
for i in range(4):
	for j in range(4):
		x = ['0']*16
		for k in range(9):
			if b[k] and -1 < i+c[k][0] < 4 and -1 < j+c[k][1] < 4:
				x[4*(i+c[k][0])+(j+c[k][1])] = '1'
		d.append(int(''.join(x), 2))

s = set([a])
q = deque([(a,0)])
done = False

while len(q) > 0:
	x, ans = q.popleft()
	if x == 0 or x == 65535:
		print ans
		done = True
		break
	for y in d:
		z = x^y
		if z not in s:
			s.add(z)
			q.append((z, ans+1))

if not done:
	print 'Impossible'
