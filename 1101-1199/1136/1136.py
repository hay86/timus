import sys
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.read().split()]
m = [] + p
m.sort()

def search(ps, pe, ms, me):
	if ps >= pe:
		return
	for i in range(ms, me):
		if m[i] == p[pe-1]:
			break
	search(pe-me+i, pe-1, i+1, me)
	search(ps, ps-ms+i, ms, i)
	print m[i],
	
search(0, n, 0, n)
