import sys

n, k, m = [int(x) for x in sys.stdin.readline().split()]

print 'YES'
for line in sys.stdin:
	start = line.find(' ')+1
	end = len(line)
	sum = 0
	num = 0
	for i in range(start, end):
		if '0' <= line[i] <= '9':
			num = num*10 + ord(line[i]) - ord('0')
		else:
			sum = (sum + num) % m
			num = 0
	print (sum + num) % m + 1