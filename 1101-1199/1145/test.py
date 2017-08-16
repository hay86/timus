import sys
print '1000 1000'

for i in range(1000):
	for j in range(1000):
		if i == 0 or i == 999 or j == 0 or j == 999 or (i%4 == 0 and j > 1) or (i%4 == 2 and j < 998):
			sys.stdout.write('#')
		else:
			sys.stdout.write('.')
	print
