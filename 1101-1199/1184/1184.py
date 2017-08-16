import sys

n, k = [int(x) for x in sys.stdin.readline().split()]
m = [int(float(x)*100) for x in sys.stdin.read().split()]

m.sort(reverse=True)
mb = sum(m)/k
ms = m[0]/k

ans = 0
while ms <= mb:
	mm = (ms+mb)/2
	if mm == 0:
		break
	total = 0
	for i in range(n):
		if m[i] >= mm:
			total += m[i]/mm
		else:
			break
	if total >= k:
		ans = mm
		ms = mm+1
	else:
		mb = mm-1
	
print '%.2f'%(ans/100.0)