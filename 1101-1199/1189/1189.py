import sys

n = int(sys.stdin.readline())
q1, q2 = [(0, '')], []
m = n
ans = []

while m > 0:
	r = m % 10
	m = m / 10
	for a, b in q1:
		aa = 0
		rr = r + a
		if rr < 0:
			aa = -1
			rr += 10
		for i in range(10):
			j = rr - i
			if j < 0:
				aa = -1
				j += 10
			if i == j:
				bb = str(i) + b
				q2.append((aa, bb))
			else:
				a0, b0 = str(i) + str(j) + b, str(i) + b
				if len(a0) > len(b0):
					c0 = 10**len(str(a0)) + 10**len(str(b0))
					if (n - int(a0) - int(b0)) % c0 == 0:
						x0 = (n - int(a0) - int(b0)) / c0
						ans.append((int(str(x0) + str(a0)), int(str(x0) + str(b0))))
	q1, q2 = q2, []
	
ans.sort(key=lambda x:x[0])

print len(ans)
for a, b in ans:
	f = '%d + %0' + str(len(str(a))-1) + 'd = %d'
	print f % (a, b, n)