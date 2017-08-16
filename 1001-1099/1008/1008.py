import sys

img = [[False for i in range(12)] for j in range(12)]

def one():
	for i in range(n):
		x, y = [int(j) for j in sys.stdin.readline().split()]
		img[x][y] = True
		if i == 0:
			x0, y0 = x, y

	v = [[False for i in range(12)] for j in range(12)]
	q = [(x0, y0)]
	v[x0][y0] = True

	print '%d %d' % (x0, y0)

	while len(q) > 0:
		x, y = q.pop(0)
		o = ''
		if img[x+1][y] and not v[x+1][y]:
			o += 'R'
			q.append((x+1, y))
			v[x+1][y] = True
		if img[x][y+1] and not v[x][y+1]:
			o += 'T'
			q.append((x, y+1))
			v[x][y+1] = True
		if img[x-1][y] and not v[x-1][y]:
			o += 'L'
			q.append((x-1, y))
			v[x-1][y] = True
		if img[x][y-1] and not v[x][y-1]:
			o += 'B'
			q.append((x, y-1))
			v[x][y-1] = True
		if len(q) == 0:
			print '.'
		else:
			print o+','
	
def two():
	xn, yn = x0, y0
	xm, ym = x0, y0
	count = 1
	q=[(x0, y0)]
	img[x0][y0] = True
	for line in sys.stdin:
		if '.' in line:
			break
		x, y = q.pop(0)
		if 'R' in line:
			q.append((x+1, y))
			count += 1
			img[x+1][y] = True
			xm = max(xm, x+1)
		if 'T' in line:
			q.append((x, y+1))
			count += 1
			img[x][y+1] = True
			ym = max(ym, y+1)
		if 'L' in line:
			q.append((x-1, y))
			count += 1
			img[x-1][y] = True
			xn = min(xn, x-1)
		if 'B' in line:
			q.append((x, y-1))
			count += 1
			img[x][y-1] = True
			yn = min(yn, y-1)
	print count
	for x in range(xn, xm+1):
		for y in range(yn, ym+1):
			if img[x][y]:
				print x, y

line = sys.stdin.readline()
if not ' ' in line:
	n = int(line)
	one()
else:
	x0, y0 = [int(y) for y in line.split()]
	two()
