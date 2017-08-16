import sys

def count_sequence(s):
	ret = {}
	stk = [1]
	n = 1
	i = len(s)-1
	while i >= 0:
		if s[i] == '(':
			if len(stk) > 0:
				stk.pop()
		elif s[i] == ')':
			stk.append(stk[-1]*n)
			n = 1
		elif '0' <= s[i] <= '9':
			j, m = i-1, int(s[i])
			while j >= 0 and '0' <= s[j] <= '9':
				m = int(s[j]) * 10**(i-j) + m
				j -= 1
			i, n = j+1, m
		else:
			chem = s[i]
			if i-1 >= 0 and 'a' <= chem <= 'z':
				i -= 1
				chem = s[i] + chem
			ret[chem] = ret.get(chem, 0) + n*stk[-1]
			n = 1
		i -= 1
	return ret

def count_formula(s):
	#print s
	arr = s.split('+')
	a = {}
	for seq in arr:
		if seq[0] < '0' or seq[0] > '9':
			seq = '1'+seq
		n, i = 0, 0
		while i < len(seq) and '0' <= seq[i] <= '9':
			n = 10*n + int(seq[i])
			i += 1
		b = count_sequence(seq[i:])
		#print { k: n*b.get(k) for k in b }
		a = { k: a.get(k, 0) + n*b.get(k, 0) for k in set(a) | set(b) }
	#print a
	return a

left = sys.stdin.readline().strip()
num = int(sys.stdin.readline())
lcount = count_formula(left)

for i in range(num):
	right = sys.stdin.readline().strip()
	rcount = count_formula(right)
	op = '==' if lcount == rcount else '!='
	print left+op+right
