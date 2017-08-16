import sys,heapq

n = int(sys.stdin.readline())

beg = [(0, 0)]
end = [(1000000000, 0)]
col = {0:'w'}

for i in range(n):
	a, b, c = sys.stdin.readline().split()
	beg.append((int(a), i+1))
	end.append((int(b), i+1))
	col[i+1] = c

def cmp(a, b):
	if a[0] == b[0]:
		return b[1] - a[1]
	return a[0] - b[0]

beg = sorted(beg, cmp=cmp)
end = sorted(end, cmp=cmp)

q = []

def push(h):
	heapq.heappush(q, 1000000000-h)

def pop():
	return 1000000000 - heapq.heappop(q)

def size():
	return len(q)

pb, pe = 0, 0
mh, mc = -1, 'w'
cov = set()
mp, ms, me = -1, -1, -1
m = 0
seq2 = []

while pb < len(beg) or pe < len(end):
	if pb == len(beg):
		x, h = end[pe]
		pe += 1
	elif pe == len(end):
		x, h = beg[pb]
		pb += 1
	elif beg[pb][0] <= end[pe][0]:
		x, h = beg[pb]
		pb += 1
	else:
		x, h = end[pe]
		pe += 1
	if h in cov:
		cov.remove(h)
		if h == mh:
			mh = pop()
			while not mh in cov and size() > 0:
				mh = pop()
			push(mh)
			mc = col[mh]
			if len(seq2) > 0 and seq2[-1][0] == x:
				seq2[-1] = (x, mh, mc)
			else:
				seq2.append((x, mh, mc))
	else:
		cov.add(h)
		push(h)
		if h > mh:
			mh, mc = h, col[h]
			seq2.append((x, mh, mc))

#for x in seq2:
#	print x

for x, mh, mc in seq2:
	if mc == 'w' and mp == -1:
		mp = x
	elif (mc == 'b' or x == 1000000000) and mp != -1:
		if x - mp > m:
			m = x - mp
			ms = mp
			me = x
		mp = -1
print ms, me
