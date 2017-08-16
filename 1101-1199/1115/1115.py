import sys, random

n, m = [int(x) for x in sys.stdin.readline().split()]
a = []
s = []

for i in range(n):
	a.append(int(sys.stdin.readline()))
for i in range(m):
	s.append(int(sys.stdin.readline()))

vis = 0
ans = []
done = False
count = 0
a.sort(reverse=True)

while not done:
	count += 1
	for i in range(m):
		size = s[i]
		b = [[0]*(n+1) for i in range(size+1)]
		c = [[0]*(n+1) for i in range(size+1)]
	
		for j in range(size+1):
			b[j][0] = j
	
		for j in range(1, size+1):
			for k in range(1, n+1):
				if a[k-1] <= j and b[j-a[k-1]][k-1] < b[j][k-1] and (vis>>(k-1))%2 == 0:
					b[j][k] = b[j-a[k-1]][k-1]
					c[j][k] = c[j-a[k-1]][k-1] | 1<<(k-1)
				else:
					b[j][k] = b[j][k-1]
					c[j][k] = c[j][k-1]
	
		if b[size][n] != 0:
			vis = 0
			ans = []
			if count == 1:
				a.sort()
			else:
				random.shuffle(a)
			done = False
			break
		else:
			done = True
		 	row= []
			for j in range(1, n+1):
				if (c[size][n]>>(j-1))%2 == 1:
					row.append(a[j-1])
					vis |= 1<<(j-1)
			ans.append(row)

for row in ans:
	print len(row)
	print ' '.join([str(x) for x in row])
