import sys

n = int(sys.stdin.readline())

root = [i for i in range(7)]
degree = [0 for i in range(7)]

def r(x):
	while x != root[x]:
		x = root[x]
	return x
	
for i in range(n):
	a, b = [int(j) for j in sys.stdin.readline().split()]
	degree[a] += 1
	degree[b] += 1
	ra = r(a)
	rb = r(b)
	if ra != rb:
		root[ra] = rb
	
def search(root, degree):
	rmap = {}
	odd = []
	for i in range(1, 7):
		if degree[i] == 0:
			continue
		if degree[i]%2 == 1:
			odd.append(i)
		ri = r(i)
		if ri not in rmap:
			rmap[ri] = []
		rmap[ri].append(i)
	k = rmap.keys()
	
	if len(k) == 1:
		total = 0
		result = []
		for i in range(0, len(odd)-2, 2):
			total += odd[i]+odd[i+1]
			result.append((odd[i], odd[i+1]))
		return total, result
	else:
		r0, r1 = k[0], k[1]
		e0, e1 = rmap[r0], rmap[r1]
		total = sys.maxint
		result = []
		for i in e0:
			for j in e1:
				root[r0] = r1
				degree[i] += 1
				degree[j] += 1
				total2, result2 = search(root, degree)
				if total2 + i + j < total:
					total = total2 + i + j
					result = [(i, j)] + result2
				root[r0] = r0
				degree[i] -= 1
				degree[j] -= 1
		return total, result

total, result = search(root, degree)
print total
print len(result)
for a, b in result:
	print a, b