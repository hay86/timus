# f[i,j] = min{ 
#	f[i+1,j-1]	(s[i]s[j]='()' or '[]')
#	f[i+1,j]+1	(s[i]='(' or '[')
#	f[i,j-1]+1	(s[j]=')' or ']')
#	f[i,k]+f[k+1,j] 
# }

import sys

a = sys.stdin.readline().strip()
n = len(a)
b = [['']*(n+1)]

for i in range(1, n+1):
	c = []
	for j in range(n+1-i):
		k = j+i-1
		minlen = sys.maxint
		minstr = None
		if a[j] == '(' and a[k] == ')' or a[j] == '[' and a[k] == ']':
			minlen = len(b[i-2][j+1]) + 2
			minstr = a[j] + b[i-2][j+1] + a[k]
		if a[j] == '(' or a[j] == '[':
			tmp = len(b[i-1][j+1]) + 2
			if tmp < minlen:
				minlen = tmp
				minstr = a[j] + b[i-1][j+1] + (')' if a[j] == '(' else ']')
		if a[k] == ')' or a[k] == ']':
			tmp = len(b[i-1][j]) + 2
			if tmp < minlen:
				minlen = tmp
				minstr = ('(' if a[k] == ')' else '[') + b[i-1][j] + a[k]
		for k in range(1, i):
			tmp = b[k][j] + b[i-k][j+k]
			if minlen > len(tmp):
				minlen = len(tmp)
				minstr = tmp
		c.append(minstr)
	b.append(c)

print b[-1][0]