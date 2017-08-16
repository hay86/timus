import sys

line = list(sys.stdin.readline().strip())

l = len(line)
s = (l-1)/2
e = True

for i in range(s, -1, -1):
	j = l-1-i
	if line[i] != line[j]:
		if e and line[i] < line[j]:
			t = s
			while t >= 0:
				if line[t] == '9':
					line[t] = '0'
					line[l-t-1] = '0'
					t -= 1
				else:
					line[t] = chr(ord(line[t])+1)
					line[l-t-1] = line[t]
					break
			line[j] = line[i]
		else:
			line[j] = line[i]
		e = False
print ''.join(line)
