import sys

n = int(sys.stdin.readline())
ret = {}
all = set()
for i in range(1, n+1):
	v = int(sys.stdin.readline())
	ret[i] = (v, 0)
	all.add(i)
tree = {}
while True:
	child, parent = [int(x) for x in sys.stdin.readline().split()]
	if child == 0 and parent == 0:
		break
	if not parent in tree:
		tree[parent] = []
	tree[parent].append(child)
	all.remove(child)
root = all.pop()

def dfs(root):
	if not root in tree:
		return
	for child in tree[root]:
		dfs(child)
	a, b = ret[root]
	for child in tree[root]:
		a += ret[child][1]
		b += max(ret[child])
	ret[root] = (a, b)
	
def dfs2(root):
	stack = [(root, False)]
	while len(stack) > 0:
		node, flat = stack[-1]
		if not flat:
			stack[-1] = (node, True)
			if node in tree:
				for child in tree[node]:
					stack.append((child, False))
		else:
			stack.pop()
			if node in tree:
				a, b = ret[node]
				for child in tree[node]:
					a += ret[child][1]
					b += max(ret[child])
				ret[node] = (a, b)
	
dfs2(root)
print max(ret[root])