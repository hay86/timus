import sys

line = ''.join(sys.stdin.readlines())

stop = ['.', '?', '!']
prev = '.'

a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')

def isletter(ch):
	return a <= ord(ch) <= z or A <= ord(ch) <= Z

def issmall(ch):
	return a <= ord(ch) <= z

count = 0
first = None

for i in range(len(line)):
	ch = line[i]
	if isletter(ch):
		if first == None:
			first = ch
			if issmall(ch):
				count += 1
		if not issmall(ch):
			if isletter(prev):
				count += 1
	elif ch in stop:
		first = None
	prev = ch

print count
