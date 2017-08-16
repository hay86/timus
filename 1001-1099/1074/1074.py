import sys, re

p = re.compile('^[\\+\\-]?([0-9]*\\.)?[0-9]+([eE][\\+\\-]?[0-9]+)?$')
p2 = re.compile('^0(\\.[0]+)?$')

while True:
	line = sys.stdin.readline()
	line = line.replace('\r','').replace('\n','')
	if line == '#':
		break
	n = int(sys.stdin.readline())
	if not p.match(line):
		print 'Not a floating point number'
		continue
	if 'e' in line:
		e = int(line[line.find('e')+1:])
		line = line[0:line.find('e')]
	elif 'E' in line:
		e = int(line[line.find('E')+1:])
		line = line[0:line.find('E')]
	else:
		e = 0
	if '.' in line:
		e += line.find('.') + 1 - len(line)
		line = line.replace('.','')
	if e < -200:
		e = -200
	elif e > 200:
		e = 200
	d = int(line)
	num = list(str(d))
	sign = ''
	if num[0] == '-':
		sign = '-'
		num = num[1:]
	if e >= 0:
		if d != 0:
			for i in range(e):
				num.append('0')
	elif -len(num) < e < 0:
		num.insert(len(num)+e, '.')
	else:
		num2 = ['0','.']
		for i in range(-e-len(num)):
			num2.append('0')
		num = num2 + num
	if '.' not in num:
		if n > 0:
			num.append('.')
			for i in range(n):
				num.append('0')
	else:
		f = len(num) - num.index('.') - 1
		for i in range(n-f):
			num.append('0')
	if n == 0:
		if '.' not in num:
			num = ''.join(num)
		else:
			num = ''.join(num[0:num.index('.')])
	else:
		num = ''.join(num[0:num.index('.')+n+1])
	if p2.match(num):
		print num
	else:
		print sign+num