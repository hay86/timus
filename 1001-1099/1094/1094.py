import sys

line = sys.stdin.readline()
p = 0
buf = [' ' for i in range(80)]

for ch in line:
	if ch == "\r" or ch == "\n":
		continue
	if ch == '>':
		p += 1
		if p > 79:
			p = 0
	elif ch == '<':
		p -= 1
		if p < 0:
			p = 0
	else:
		buf[p] = ch
		p += 1
		if p > 79:
			p = 0
print ''.join(buf)