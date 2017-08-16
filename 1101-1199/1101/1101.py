import sys

op, rpn = [], []
pos = {}
exp = sys.stdin.readline().strip()

while len(exp) > 0:
	if exp.startswith('('):
		op.append('(')
		exp = exp[1:].strip()
	elif exp.startswith(')'):
		x = op.pop()
		while x is not '(':
			rpn.append(x)
			x = op.pop()
		exp = exp[1:].strip()
	elif exp.startswith('NOT'):
		op.append('!')
		exp = exp[3:].strip()
	elif exp.startswith('AND'):
		for x in ['!']:
			while len(op) > 0 and op[-1] is x:
				op.pop()
				rpn.append(x)
		op.append('&')
		exp = exp[3:].strip()
	elif exp.startswith('OR'):
		for x in ['!','&']:
			while len(op) > 0 and op[-1] is x:
				op.pop()
				rpn.append(x)
		op.append('|')
		exp = exp[2:].strip()
	elif exp.startswith('TRUE'):
		rpn.append(1)
		exp = exp[4:].strip()
	elif exp.startswith('FALSE'):
		rpn.append(0)
		exp = exp[5:].strip()
	else:
		x = exp[0]
		if x not in pos:
			pos[x] = []
		pos[x].append(len(rpn))
		rpn.append(0)
		exp = exp[1:].strip()

op.reverse()
rpn.extend(op)

n, m, k = [int(x) for x in sys.stdin.readline().split()]
fork = set()
invert = {}

for i in range(m):
	line = sys.stdin.readline().strip()
	fork.add(line)

for i in range(k):
	line = sys.stdin.readline().strip()
	x = line.rfind(' ')
	invert[line[:x].strip()] = line[x:].strip()

cur = [0, 0]
mv = (1, 0)
right = {(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1),(0,1):(1,0)}
left = {(0,-1):(1,0),(-1,0):(0,-1),(0,1):(-1,0),(1,0):(0,1)}

while -n <= cur[0] <= n and -n <= cur[1] <= n:
	print cur[0], cur[1]
	cur[0] += mv[0]
	cur[1] += mv[1]
	out = '%d %d' % (cur[0], cur[1])
	if out in invert:
		reg = invert[out]
		if reg in pos:
			for i in pos[reg]:
				rpn[i] = 1 - rpn[i]
	elif out in fork:
		stk = []
		for c in rpn:
			if c is '!':
				stk[-1] = 1 - stk[-1]
			elif c is '&':
				stk[-2] &= stk[-1]
				stk.pop()
			elif c is '|':
				stk[-2] |= stk[-1]
				stk.pop()
			else:
				stk.append(c)
		if stk[0] == 1:
			mv = right[mv]
		else:
			mv = left[mv]
