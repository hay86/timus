import random

n = []
m = []

for r in range(10):
	c = random.randint(1, 20)
	k = 0
	for i in range(c):
		j = random.randint(1, 100)
		k += j
		n.append(j)
	m.append(k)

random.shuffle(n)
random.shuffle(m)

print len(n), len(m)
for x in n:
	print x
for x in m:
	print x
