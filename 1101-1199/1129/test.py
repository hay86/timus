import random

n = random.randint(1,10)

s = {}
t = random.randint(0,n*n/2)

for i in range(t):
	a = random.randint(1,n)
	b = random.randint(1,n)
	if a == b:
		continue
	if a > b:
		a, b = b, a
	if a-1 not in s:
		s[a-1] = set()
	if b-1 not in s:
		s[b-1] = set()
	s[a-1].add(b)
	s[b-1].add(a)

print n
for i in range(n):
	x = [] if i not in s else list(s[i])
	x.sort()
	print len(x),
	for j in x:
		print j,
	print
