import sys

i, j = [int(x) for x in sys.stdin.readline().split()]

if i == 1 or i==j:
	print i
else:
	ratio = sys.maxint
	ans = 0
	for k in xrange(j, i-1, -1):
		sum = 0
		div = 2
		for div in xrange(2, k):
			if div*div > k:
				break
			if k%div == 0:
				sum += div
				if k/div != div:
					sum += k/div
		if float(sum)/k < ratio:
			ratio = float(sum)/k
			ans = k
		if ratio == 0:
			break
	print ans
