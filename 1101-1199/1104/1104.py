import sys

t, b = 0, 0
d0, da = ord('0'), ord('A')-10

for ch in sys.stdin.readline().strip():
	if ch <= '9':
		a = ord(ch) - d0
		t += a
		if b < a:
			b = a
	else:
		a = ord(ch) - da
		t += a
		if b < a:
			b = a

success = False
for i in range(b, 36):
	if i > 0 and t%i == 0:
		print i+1
		success = True
		break
if not success:
	print 'No solution.'
