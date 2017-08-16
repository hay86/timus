import sys

a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]

x, y = 3*a[0] - 2, 3*b[0] - 2
i, j = 1, 1
ans = []

while i <= x and j <= y:
	x1, y1, v1 = a[i], a[i+1], a[i+2]
	x2, y2, v2 = b[j], b[j+1], b[j+2]
	if x1 == x2:
		if y1 == y2:
			i += 3
			j += 3
		elif y1 > y2:
			a[i] = y2
			j + 3
		else:
			i += 3
	elif y1 == y2:
		if x1 > x2:
			i += 3
			j += 3
		else:
			ans.append((x1, x2, v1))
			i += 3
			j += 3
	elif y2 <= x1:
		j += 3
	elif y1 <= x2:
		ans.append((x1, y1, v1))
		i += 3
	elif x2 < x1 and y1 < y2:
		i += 3
	elif x1 < x2 and y2 < y1:
		ans.append((x1, x2, v1))
		a[i] = y2
		j += 3
	elif x2 < x1:
		a[i] = y2
		j += 3
	else:
		ans.append((x1, x2, v1))
		i += 3
		
while i <= x:
	ans.append((a[i], a[i+1], a[i+2]))
	i += 3	
	
print len(ans),
for k in ans:
	print k[0], k[1], k[2],