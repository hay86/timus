import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
a = [False]*(n*m)
b = [False]*(n*m)
k1 = -1

for i in range(m):
	line = sys.stdin.readline()
	for j in range(n):
		if line[j] == '.':
			k1 = i*n+j
			a[k1] = True
			b[k1] = True

def bfs(i, t):
	q1 = [-1]*(n*m)
	q2 = [-1]*(n*m)
	q1[0], q2[0] = i, 1
	s, e = 0, 1
	t[i] = False
	while s < e:
		j, l = q1[s], q2[s]
		s += 1
		if j%n != 0 and t[j-1]:
			q1[e] = j-1
			q2[e] = l+1
			e += 1
			t[j-1] = False
		if j%n != n-1 and t[j+1]:
			q1[e] = j+1
			q2[e] = l+1
			e += 1
			t[j+1] = False
		if j >= n and t[j-n]:
			q1[e] = j-n
			q2[e] = l+1
			e += 1
			t[j-n] = False
		if j <= (m-1)*n-1 and t[j+n]:
			q1[e] = j+n
			q2[e] = l+1
			e += 1
			t[j+n] = False
	return j, l

k2, d1 = bfs(k1, a)
k3, d2 = bfs(k2, b)

print max(d1, d2)-1
	
