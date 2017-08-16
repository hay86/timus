import sys, math

a, b = [int(x) for x in sys.stdin.readline().split()]
c = [0]*31

for i in range(2, 31):
	for j in range(i):
		c[i] += 2**j*(i-j-1)

def foo(i):
	j = math.log(i, 2)
	if j == 0:
		return 0
	elif int(j) == j:
		return c[int(j)]
	else:
		return c[int(j)] + int(j)-1 + foo(i-2**int(j))

print foo(b) - foo(a) if b > a else foo(a) - foo(b)
