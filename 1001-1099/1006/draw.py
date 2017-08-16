# coding=utf8
import sys

n = int(sys.stdin.readline())

m = [['.' for i in range(50)] for j in range(20)]

for i in range(n):
	y, x, a = [int(j) for j in sys.stdin.readline().split()]
	m[x][y] = u'┌'
	m[x][y+a-1] = u'┐'
	m[x+a-1][y+a-1] = u'┘'
	m[x+a-1][y] = u'└'
	for j in range(1, a-1):
		m[x+j][y] = u'│'
		m[x+j][y+a-1] = u'│'
		m[x][y+j] = u'─'
		m[x+a-1][y+j] = u'─'

for i in range(20):
	for j in range(50):
		print '%s' % m[i][j].encode('utf8'),
	print
