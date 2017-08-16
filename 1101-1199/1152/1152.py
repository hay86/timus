import sys, random

n = int(sys.stdin.readline())
m = [int(x) for x in sys.stdin.readline().split()]
ans = 9999

def dfs(left, hurt):
	global ans
	for i in range(n):
		l = i-1 if i>0 else n-1
		r = i+1 if i<n-1 else 0
		val = m[l]+m[i]+m[r]
		if val > 0:
			tmp = left-val
			if tmp == 0:
				ans = min(ans, hurt)
			elif hurt+tmp < ans:
				m1, m2, m3 = m[l], m[i], m[r]
				m[l], m[i], m[r] = 0, 0, 0
				dfs(tmp, hurt+tmp)
				m[l], m[i], m[r] = m1, m2, m3

dfs(sum(m), 0)
print ans


