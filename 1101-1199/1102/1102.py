import sys

n = int(sys.stdin.readline())

for line in sys.stdin:
	i = len(line)-1
	while line[i] == '\r' or line[i] == '\n':
		i -= 1
	ok = True
	while i >= 0:
		if line[i] == 'e':
			if i >= 2 and line[i-1] == 'n' and line[i-2] == 'o':
				i -= 3
			else:
				ok = False
				break
		elif line[i] == 'n':
			if i >= 1 and line[i-1] == 'i':
				i -= 2
			elif i >= 4 and line[i-1] == 'o' and line[i-2] == 't' and line[i-3] == 'u' and line[i-4] == 'p':
				i -= 5
			else:
				ok = False
				break
		elif line[i] == 't':
			if i >= 2 and line[i-1] == 'u':
				if line[i-2] == 'o':
					i -= 3
				elif line[i-2] == 'p':
					if i >= 4 and line[i-3] == 'n' and line[i-4] == 'i':
						i -= 5
					elif i >= 5 and line[i-3] == 't' and line[i-4] == 'u' and line[i-5] == 'o':
						i -= 6
					else:
						ok = False
						break
				else:
					ok = False
					break
			else:
				ok = False
				break
		else:
			ok = False
			break
	if ok:
		print 'YES'
	else:
		print 'NO'