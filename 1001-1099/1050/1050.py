import sys

b1 = []
b2 = ['``', "''"]
c = 0
par = False

for ch in sys.stdin.read():
	asc = ord(ch)
	if not (96 < asc < 123 or 64 < asc < 91):
		if len(b1) > 3 and b1[-4] == '\\' and b1[-3] == 'p' and b1[-2] == 'a' and b1[-1] == 'r':
			par = True
	if ch == '\n':
		if (len(b1) > 0 and b1[-1] == '\n') or (len(b1) > 1 and b1[-2] == '\n' and b1[-1] == '\r'):
			par = True
	if par:
		if c == 1:
			for i in range(len(b1)-1, -1, -1):
				if b1[i] == '``':
					b1[i] = ''
					break
		if len(b1) > 0:
			sys.stdout.write(''.join(b1))
		b1 = []
		c = 0
	if ch == '"' and (len(b1) == 0 or b1[-1] != '\\'):
		b1.append(b2[c])
		c = 1-c
	else:
		b1.append(ch)
	par = False

if c == 1:
	for i in range(len(b1)-1, -1, -1):
		if b1[i] == '``':
			b1[i] = ''
			break
if len(b1) > 0:
	sys.stdout.write(''.join(b1))
