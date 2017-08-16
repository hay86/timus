import sys

n = int(sys.stdin.readline())
for i in range(n):
	a, b = list(sys.stdin.readline().strip())
	a = ord(a) - ord('a')
	b = int(b) - 1
	t = 0
	if 0<=a+2<=7 and 0<=b+1<=7:
		t+=1
	if 0<=a+2<=7 and 0<=b-1<=7:
		t+=1
	if 0<=a-2<=7 and 0<=b+1<=7:
		t+=1
	if 0<=a-2<=7 and 0<=b-1<=7:
		t+=1
	if 0<=a+1<=7 and 0<=b+2<=7:
		t+=1
	if 0<=a+1<=7 and 0<=b-2<=7:
		t+=1
	if 0<=a-1<=7 and 0<=b+2<=7:
		t+=1
	if 0<=a-1<=7 and 0<=b-2<=7:
		t+=1
	print t
