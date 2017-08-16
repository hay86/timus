import sys

n = int(sys.stdin.readline())
p = []

for i in range(n):
	x, y, z = [int(j) for j in sys.stdin.readline().split()]
	p.append((x, y, z))

for i in range(n):
	q = [(0,0),(0,sys.maxint),(sys.maxint,sys.maxint),(sys.maxint,0)]
	for j in range(n):
		if i == j:
			continue
		one = float(sys.maxint)
		a0 = (one/p[i][0]-one/p[j][0])
		b0 = (one/p[i][1]-one/p[j][1])
		c0 = (one/p[i][2]-one/p[j][2])
		tmp = []
		for k in range(len(q)):
			(x0, y0), (x1, y1) = q[k-1], q[k]
			u = x0*a0 + y0*b0 + c0
			v = x1*a0 + y1*b0 + c0
			if u < 0 and v < 0:
				tmp.append(q[k-1])
			elif u < 0 and v >= 0 or u >=0 and v < 0:
				if u < 0:
					tmp.append(q[k-1])
				if v == 0:
					tmp.append(q[k])
					continue
				if u == 0:
					tmp.append(q[k-1])
					continue
				a1, b1, c1 = y1-y0, x0-x1, x1*y0-x0*y1
				point = ((c1*b0-c0*b1) / (a0*b1-a1*b0), (c1*a0-c0*a1) / (a1*b0-a0*b1))
				tmp.append(point)
		q = tmp
	print 'Yes' if len(q) > 0 else 'No'