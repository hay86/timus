import sys

n = int(sys.stdin.readline())
m = []
m += [(0,1,3,2),(1,3,2,0),(3,2,0,1),(2,0,1,3),(0,2,3,1),(1,0,2,3),(3,1,0,2),(2,3,1,0)]
m += [(0,4,3,5),(4,3,5,0),(3,5,0,4),(5,0,4,3),(0,5,3,4),(4,0,5,3),(3,4,0,5),(5,3,4,0)]
m += [(1,4,2,5),(4,2,5,1),(2,5,1,4),(5,1,4,2),(1,5,2,4),(4,1,5,2),(2,4,1,5),(5,2,4,1)]
s = {}

for line in sys.stdin:
	for i,j,k,l in m:
		hash = line[i]+line[j]+line[k]+line[l]
		if hash in s:
			s[hash] += 1
		else:
			s[hash] = 1
	
ans = 0	
for k,v in s.items():
	if v > ans:
		ans = v
		
print ans