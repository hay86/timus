import sys, random

l = int(sys.argv[1])
n = random.randint(1,l)
m = random.randint(1,l)
p = random.randint(0,10)

c = [0,1,2,3,4,5,6,7,8,9]
s = []

for i in range(p):
	t = ''
	for j in range(random.randint(1,m)):
		t += str(c[random.randint(0,n-1)])
	s.append(t)

with open('7.in','w') as f:
	f.write('%d %d %d\n' % (n, m, p))
	f.write(''.join([str(xxx) for xxx in c[:n]]))
	for ss in s:
		f.write('\n')
		f.write(ss)


x = [-1]*m
k = 0
r = 0
while k >= 0:
	while x[k] < c[n-1]:
		x[k] += 1
		if k == m-1:
			xx = ''.join([str(xxx) for xxx in x])
			f = True
			for ss in s:
				if ss in xx:
					f = False
					break
			if f:
				r += 1
		else:
			k += 1
	x[k] = -1
	k -= 1

print r
