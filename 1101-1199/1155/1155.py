import sys

line = sys.stdin.read()
a = [int(x) for x in line.strip().split(' ')]

if sum(a) % 2 == 1:
	print 'IMPOSSIBLE'
else:
	b = [(0,1,'AB-'),(0,3,'AD-'),(0,4,'AE-'),(1,2,'BC-'),(1,5,'BF-'),(2,3,'CD-'),(2,6,'CG-'),(3,7,'DH-'),(4,5,'EF-'),(4,7,'EH-'),(5,6,'FG-'),(6,7,'GH-')]
	c = []
	for x,y,z in b:
		n = min(a[x],a[y])
		if n > 0:
			c.append((z, n))
			a[x] -= n
			a[y] -= n
	b = [(0,6,'BC+','AB-','CG-'),(1,7,'CD+','BC-','DH-'),(2,4,'AB+','BC-','AE-'),(3,5,'BC+','CD-','BF-')]
	for x,y,z0,z1,z2 in b:
		if a[x] > 0 and a[x] == a[y]:
			c.append((z0, a[x]))
			c.append((z1, a[x]))
			c.append((z2, a[x]))
			a[x], a[y] = 0, 0
	if sum(a) > 0:
		print 'IMPOSSIBLE'
	else:
		for x,y in c:
			for i in range(y):
				print x