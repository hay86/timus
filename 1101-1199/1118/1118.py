import sys

i, j = [int(x) for x in sys.stdin.readline().split()]

if i == 1 or i==j:
	print i
else:
	if j%2 == 0:
		j -= 1
	num = 0
	min_sum = sys.maxint
	while j >= i:
		d = int(j**0.5)+1
		sum = 0
		for k in range(3, d, 2):
			if j%k == 0:
				sum += 1.0/k + float(k)/j
				if sum >= min_sum:
					break
		if sum == 0:
			num = j
			break
		elif sum < min_sum:
			min_sum = sum
			num = j
		j -= 2
	print num
