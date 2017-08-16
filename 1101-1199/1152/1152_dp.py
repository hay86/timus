import sys

n = int(sys.stdin.readline())
m = [int(x) for x in sys.stdin.readline().split()]
dp = [9999]*(1<<n)
dp[0] = 0

def dfs(st, left):
	if dp[st] < 9999:
		return dp[st]
	for i in range(n):
		if st & (1<<i):
			tmp = st
			l = i-1 if i > 0 else n-1
			r = i+1 if i < n-1 else 0
			tmp -= (1<<i)
			destory = m[i]
			if tmp & (1<<l):
				tmp -= (1<<l)
				destory += m[l]
			if tmp & (1<<r):
				tmp -= (1<<r)
				destory += m[r]
			dp[st] = min(dp[st], dfs(tmp, left-destory)+left-destory)
	return dp[st]

dfs((1<<n)-1, sum(m))
print dp[(1<<n)-1]
