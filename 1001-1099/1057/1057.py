import sys
x, y = [int(x) for x in sys.stdin.readline().split()]
k = int(sys.stdin.readline())
b = int(sys.stdin.readline())

xx = []
yy = []

while x > 0:
	xx.insert(0, x%b)
	x = int(x/b)
while y > 0:
	yy.insert(0, y%b)
	y = int(y/b)

for i in range(len(yy)-len(xx)):
	xx.insert(0, 0)

def C(a, b):
	x1, x2 = (a, b-a) if a < b-a else (b-a, a)
	c = 1
	for i in range(x2+1, b+1):
		c *= i
	for i in range(2, x1+1):
		c /= i
	return c

t1, c = 0, 0
for i in range(len(xx)):
	if xx[i] == 1:
		c += 1
		if k-c == 0:
			if sum(xx[i+1:]) == 0:
				t1 += 1
			break
	elif xx[i] == 0 and len(xx)-i-1 >= k-c-1:
		t1 += C(k-c-1, len(xx)-i-1)
	else:
		break

t2, c = 0, 0
for i in range(len(yy)):
	if yy[i] == 1:
		c += 1
		if k-c == 0:
			break
	elif yy[i] == 0 and len(yy)-i-1 >= k-c-1:
		t2 += C(k-c-1, len(yy)-i-1)
	else:
		break

print t1 - t2
