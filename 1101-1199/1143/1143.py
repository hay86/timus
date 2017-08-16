import sys

n = int(sys.stdin.readline())
m = [[0]*n for i in range(n)]
a = []

for i in range(n):
	p = sys.stdin.readline().split(' ')
	a.append((float(p[0]),float(p[1])))
	for j in range(i):
		dist = ((a[i][0]-a[j][0])**2+(a[i][1]-a[j][1])**2)**.5
		m[i][j] = dist
		m[j][i] = dist

s = [[0]*n for i in range(n)]
e = [[0]*n for i in range(n)]

for i in range(1, n):
	for j in range(n):
		s[i][j] = min(s[i-1][(j+1)%n] + m[j][(j+1)%n], e[i-1][(j+i)%n] + m[j][(j+i)%n])
		e[i][j] = min(e[i-1][(j-1)%n] + m[j][(j-1)%n], s[i-1][(j-i)%n] + m[j][(j-i)%n])
		
print '%.3f' % min(s[n-1])