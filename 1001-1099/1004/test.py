import random

n = random.randint(3, 20)
m = random.randint(3, 100)

print n, m

for i in range(m):
	a, b = 1, 1
	while a == b:
		a = random.randint(1,n)
		b = random.randint(1,n)
	c = random.randint(1,300)
	print a, b, c

print -1
