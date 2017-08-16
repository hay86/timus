import sys

m, n = [int(x) for x in sys.stdin.readline().split()]
root = [i for i in range(m)]
ans = 0

def find(i):
	if root[i] == i:
		return i
	else:
		root[i] = find(root[i])
		return root[i]
	
for i in range(m):
	line = [int(x) for x in sys.stdin.readline().split()]
	done = True
	for c in line:
		if c-1 != i:
			ans += 1
			root[find(c-1)] = find(i)
			done = False
	if done:
		root[i] = -1

for i in range(m):
	if i == root[i]:
		ans += 1
		
print ans-1 if ans > 0 else 0