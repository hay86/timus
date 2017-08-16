import sys

n = int(sys.stdin.readline())
m = [[[[0,0,0] for i in range(n+1)] for i in range(n+1)] for i in range(n+1)]
m[n][n][n][0] = 1

for i in range(1,3*n+1):
	for j in range(max(0,i-2*n),min(n,i)+1):
		for k in range(max(0,i-j-n),min(n,i-j)+1):
			x, y, z = n-j, n-k, n-i+j+k
			for s in range(3): 
				if s != 0 and x+1 <= n:
					m[x][y][z][s] += m[x+1][y][z][0]
				if s != 1 and y+1 <= n:
					m[x][y][z][s] += m[x][y+1][z][1]
				if s != 2 and z+1 <= n:
					m[x][y][z][s] += m[x][y][z+1][2]

ans = m[0][0][0][0]
for i in range(2,n+1):
	ans *= i*i*(i-1)
print ans/2
