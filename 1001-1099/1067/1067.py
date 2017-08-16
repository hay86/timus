import sys

n = int(sys.stdin.readline())
map = {}

def prt(ind, parent, child):
	print ind + child
	key = tuple(list(parent) + [child])
	if key in map:
		name = list(map[key])
		name.sort()
		for sub in name:
			prt(ind + ' ',  key, sub)

root = set()
for i in range(n):
	path = sys.stdin.readline().strip().split('\\')
	root.add(path[0])
	for j in range(len(path)-1):
		key = tuple(path[0:j+1])
		if not key in map:
			map[key] = set()
		map[key].add(path[j+1])

root = list(root)
root.sort()
for r in root:
	prt('', (), r)