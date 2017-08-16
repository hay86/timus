import sys

m = []
for line in sys.stdin:
	m.append(list(line.strip()))
	
def check(m):
	for c in ['X', 'O']:
		for i in range(3):
			if m[i][0] == c and m[i][1] == c and m[i][2] == c:
				return c
			if m[0][i] == c and m[1][i] == c and m[2][i] == c:
				return c
		if m[0][0] == c and m[1][1] == c and m[2][2] == c:
			return c
		if m[0][2] == c and m[1][1] == c and m[2][0] == c:
			return c
	for i in range(3):
		if '#' in m[i]:
			return None
	return 'Draw'

def dfs(m, c):
	result = check(m)
	if result == 'X':
		return 'Crosses win'
	elif result == 'O':
		return 'Ouths win'
	elif result == 'Draw':
		return 'Draw'
	result = 'Ouths win' if c == 'X' else 'Crosses win'
	for i in range(3):
		for j in range(3):
			if m[i][j] == '#':
				m[i][j] = c
				r = dfs(m, 'O' if c == 'X' else 'X')
				if c == 'X':
					if r == 'Crosses win':
						m[i][j] = '#'
						return r
					elif r == 'Draw':
						result = 'Draw'
				else:
					if r == 'Ouths win':
						m[i][j] = '#'
						return r
					elif r == 'Draw':
						result = 'Draw'
				m[i][j] = '#'
	return result
	
print dfs(m, 'X')