import sys

l, n = [int(x) for x in sys.stdin.readline().split()]
k = [int(x) for x in sys.stdin.readline().split()]

done = False
for i in range(n):
	if l < k[i]:
		done = True
		break
	else:
		l -= l%k[i]
		
print 'YES' if done else 'NO'