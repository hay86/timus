import sys

n = int(sys.stdin.readline())
m = [0]*3

for i in range(n):
	a, b = sys.stdin.readline().strip().split()
	m[ord(a)-ord('X')] += int(b)

m1 = (0, m[1]+m[0], m[2]-m[0])
m2 = (m[0]+m[1], 0, m[2]+m[1])
m3 = (m[0]-m[2], m[1]+m[2], 0)

ans = [m1, m2, m3]
ans.sort(key=lambda x: sum([abs(y) for y in x]))

num = 0
for x in ans[0]:
	if x != 0:
		num += 1
print num
for i in range(3):
	if ans[0][i] != 0:
		print chr(ord('X')+i), -ans[0][i]
