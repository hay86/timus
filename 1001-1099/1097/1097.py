import sys

l, a = [int(x) for x in sys.stdin.readline().split()]
n = int(sys.stdin.readline())

data = [(255, 0, 0, 0, 0)]

for i in range(n):
	w, s, x, y = [int(x) for x in sys.stdin.readline().split()]
	data.append((w, x, y, x+s-1, y+s-1))

small = 255

for i in range(n+1):
	for j in range(n+1):
		x0, y0 = data[i][3]+1, data[j][4]+1
		x1, y1 = x0+a-1, y0+a-1
		if x1 > l or y1 > l:
			continue
		#print x0, y0, x1, y1
		big = 1
		for k in range(n+1):
			if (x0 <= data[k][1] <= x1 or x0 <= data[k][3] <= x1) and (y0 <= data[k][2] <= y1 or y0 <= data[k][4] <= y1):
				#print data[k]
				big = max(big, data[k][0])
		small = min(small, big)
		
print small if small <= 100 else 'IMPOSSIBLE'