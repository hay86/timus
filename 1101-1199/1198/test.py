import sys, random

n = int(sys.argv[1])
print n

for i in range(n):
	#for j in range(random.randint(0, int(sys.argv[2]))):
	for j in range(int(sys.argv[2])):
		print random.randint(0, n-1) + 1,
	print 0
