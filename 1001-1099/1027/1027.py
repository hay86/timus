import sys

s = set('=+-*/0123456789)(\n')
pch = None
sym = []
com = 0
ari = 0

i = 0
for ch in sys.stdin.read():
	i += 1
	if pch == '(' and ch == '*':
		if com == 0:
			sym.append('*')
			com = i
	elif pch == '*' and ch == ')' and i > com+1:
		if com > 0:
			sym.pop()
			com = 0
		elif ari == 0:
			com = -1
			break
	if ch == '(':
		if com == 0:
			sym.append('(')
			ari += 1
	elif ch == ')':
		if com > 0:
			pass
		elif ari > 0:
			sym.pop()
			ari -= 1
		else:
			ari = -1
			break
	if com == 0 and ari > 0 and not ch in s:
		break
	pch = ch

print 'YES' if com == 0 and ari == 0 and len(sym) == 0 else 'NO'