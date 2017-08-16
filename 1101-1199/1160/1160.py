import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
a = []

for i in range(m):
	a.append([int(x) for x in sys.stdin.readline().split()])

a.sort(key=lambda x: x[2])

f = [i for i in range(n+1)]

def father(i):
	if f[i] != i:
		f[i] = father(f[i])
	return f[i]


for i in range(m):
	j = father(a[i][0])
	k = father(a[i][1])
	f[k] = j
	done = father(1)
	for j in range(2, n+1):
		if done != father(j):
			done = False
			break
	if done != False:
		break

print a[i][2]
print i+1
for j in range(i+1):
	print a[j][0], a[j][1]
