import sys

dict = set()

while True:
	word = sys.stdin.readline().strip()
	if word == '#':
		break
	dict.add(word)

def correct(w2):
	if not w2 in dict:
		for w1 in dict:
			if len(w1) == len(w2):
				c = 0
				for i in range(len(w1)):
					if w1[i] != w2[i]:
						c += 1
						if c == 2:
							break
				if c == 1:
					return (w1, 1)
	return (w2, 0)
		
mistake = 0
for line in sys.stdin.readlines():
	line = line.strip()
	start, end = 0, 0
	for i in range(len(line)):
		if ord(line[i]) > ord('z') or ord(line[i]) < ord('a'):
			if start < end:
				word = line[start:end]
				word, wrong = correct(word)
				mistake += wrong
				sys.stdout.write(word)
			sys.stdout.write(line[i])
			start = i+1
			end = i+1
		else:
			end += 1
	if start < end:
		word = line[start:end]
		word, wrong = correct(word)
		mistake += wrong
		sys.stdout.write(word)
	print
print mistake