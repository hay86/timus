import sys

i, fi, j, fj, k = [int(x) for x in sys.stdin.readline().split()]

def ab(x):
	a, b = 1, 0
	for i in range(x):
		a, b = b, a+b
	return a, b

if k == i:
	print fi
elif k == j:
	print fj
else:
	if i > j:
		i, j = j, i
		fi, fj = fj, fi
	if k < i < j:
		a1, b1 = ab(i-k)
		a2, b2 = ab(j-k)
		fk = (b2*fi-b1*fj)/(a1*b2-a2*b1)
	else:
		a1, b1 = ab(j-i)
		a2, b2 = ab(k-i)
		fk = a2*fi +b2*(fj-a1*fi)/b1
	print fk
