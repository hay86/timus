import sys

n, k = [int(x) for x in sys.stdin.readline().split()]

ans = 0
min = sys.maxint

beg = 0
len = 0
sum = 0
buf = []

i = 0
for ch in sys.stdin.read():
	if ch == '\r' or ch == '\n':
		continue
	i += 1
	if ch == '*':
		beg = 0
		len = 0
		sum = 0
		buf = []
	else:
		buf.append(int(ch))
		if beg == 0:
			beg = i
		if len < k:
			sum += buf[-1]
			len += 1
		else:
			sum += buf[-1] - buf[-k-1]
			beg += 1
		if len == k and sum < min:
			min = sum
			ans = beg
print ans