import random

f = open('4.in','w')
f.write('3\n')
for i in range(3):
	a = random.randint(1, 6)
	b = random.randint(1, 6)
	f.write('%d %d\n' % (a, b))
	print a, b
f.close()