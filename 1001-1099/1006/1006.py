import sys

screen = [[0 for i in range(50)] for i in range(20)]
corner = {}
C = {218:[1,1], 191:[1,-1], 192:[-1, 1], 217:[-1,-1]}

for i in range(20):
	line = sys.stdin.readline().strip()
	for j in range(50):
		ch = ord(line[j])
		if ch in C:
			corner[(i, j)] = ch
		screen[i][j] = ch

ans = []

while len(corner) > 0:
	(x, y), ch = corner.popitem()
	for a in range(19, 0, -1):
		c1 = (min(x, x+C[ch][0]*a), min(y, y+C[ch][1]*a))
		c2 = (c1[0] + a, c1[1] + a)
		if c1[0] < 0 or c1[1] < 0:
			continue
		if c2[0] > 19 or c2[1] > 49:
			continue
		stop = False
		for i in range(a+1):
			if screen[c1[0]+i][c1[1]] == 46:
				stop = True
				break
			if screen[c1[0]][c1[1]+i] == 46:
				stop = True
				break
			if screen[c2[0]-i][c2[1]] == 46:
				stop = True
				break
			if screen[c2[0]][c2[1]-i] == 46:
				stop = True
				break
		if not stop:
			ans.append((c1[0], c1[1], a))
			if (c1[0], c1[1]) in corner and corner[(c1[0], c1[1])] == 218:
				corner.pop((c1[0], c1[1]))
			if (c1[0], c2[1]) in corner and corner[(c1[0], c2[1])] == 191:
				corner.pop((c1[0], c2[1]))
			if (c2[0], c2[1]) in corner and corner[(c2[0], c2[1])] == 217:
				corner.pop((c2[0], c2[1]))
			if (c2[0], c1[1]) in corner and corner[(c2[0], c1[1])] == 192:
				corner.pop((c2[0], c1[1]))
			break

ans2 = []

for i in range(len(ans)):
	for j in range(len(ans)):
		if ans[j] == True:
			continue
		x, y, a = ans[j]
		if screen[x][y] != 218 and screen[x][y] != 32:
			continue
		if screen[x][y+a] != 191 and screen[x][y+a] != 32:
			continue
		if screen[x+a][y+a] != 217 and screen[x+a][y+a] != 32:
			continue
		if screen[x+a][y] != 192 and screen[x+a][y] != 32:
			continue
		stop = False
		for k in range(1, a):
			if (screen[x+k][y] != 179 and screen[x+k][y] != 32) or (screen[x+k][y+a] != 179 and screen[x+k][y+a] != 32):
				stop = True
				break
			if (screen[x][y+k] != 196 and screen[x][y+k] != 32) or (screen[x+a][y+k] != 196 and screen[x+a][y+k] != 32):
				stop= True
				break
		if stop:
			continue
		ans[j] = True
		for k in range(a+1):
			screen[x+k][y] = 32
			screen[x+k][y+a] = 32
			screen[x][y+k] = 32
			screen[x+a][y+k] = 32
		ans2.append((y, x, a+1))

for i in range(20):
	for j in range(50):
		if screen[i][j] == 196:
			for a in range(1, 19-i+1):
				if screen[i+a][j] == 196:
					for k in range(a+1):
						screen[i+k][j] = 32
						screen[i+k][j+a] = 32
						screen[i][j+k] = 32
						screen[i+a][j+k] = 32
					ans2.append((j-1, i, a+1))
					break
		if screen[i][j] == 179:
			for a in range(1, 49-j+1):
				if screen[i][j+a] == 179:
					for k in range(a+1):
						screen[i+k][j] = 32
						screen[i+k][j+a] = 32
						screen[i][j+k] = 32
						screen[i+a][j+k] = 32
					ans2.append((j, i-1, a+1))
					break

print len(ans2)
for i in range(len(ans2)-1, -1, -1):
	print ans2[i][0], ans2[i][1], ans2[i][2]
