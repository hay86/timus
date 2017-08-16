import sys

a = [False]*37
b = [0]*37

for ch in sys.stdin.read():
	if '0' <= ch <= '9':
		j = ord(ch) - ord('0')
	elif 'A' <= ch <= 'Z':
		j = ord(ch) - ord('A') + 10
	else:
		j = sys.maxint
	for i in range(2, 37):
		if j < i:
			if not a[i]:
				b[i] += 1
				a[i] = True
		else:
			if a[i]:
				a[i] = False

maxbase, maxnum = 0, 0
for i in range(2, 37):
	if b[i] > maxnum:
		maxbase = i
		maxnum = b[i]

print maxbase, maxnum
