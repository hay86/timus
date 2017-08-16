import sys

def merge_sort(i, j):
	if i == j:
		return 0
	k = int((i+j)/2)
	a = merge_sort(i, k)
	b = merge_sort(k+1, j)
	r = 0
	p = i
	p1 = i
	p2 = k+1
	while p1 <= k and p2 <= j:
		if d[p1] < d[p2]:
			dd[p] = d[p1]
			p += 1
			p1 += 1
		else:
			dd[p] = d[p2]
			p += 1
			p2 += 1
			r += k-p1+1
	if p1 <= k:
		for z in range(p1, k+1):
			d[j-(k-z)] = d[z]
	
	for z in range(i, p):
		d[z] = dd[z]
	return a + b + r

n, k = [int(x) for x in sys.stdin.readline().split()]

max_r = -1
max_s = -1

for i in range(1, k+1):
	d = [int(x) for x in sys.stdin.readline().split()]
	dd = [0 for x in range(len(d))]
	s = merge_sort(0, len(d)-1)
	if s > max_s:
		max_s = s
		max_r = i
print max_r

