import sys

def line():
	return sys.stdin.readline()

def minute(str):
	t = [int(x) for x in str.split('.')]
	return t[0]*60+t[1]
	
def ans(diff):
	diff /= 2	
	a = abs((diff+10)/60)
	b = abs((diff+10)/60)
	return int(a) if a > b else int(b)
	
dep1, arr1 = [minute(x) for x in line().split()]
dep2, arr2 = [minute(x) for x in line().split()]

diff = (arr1-dep1) - (arr2-dep2)
while diff < -900:
	diff += 1440
while diff >  900:
	diff -= 1440
diff2 = diff + 1440
diff3 = diff - 1440
	
x = ans(diff)
if 0 <= x <= 5:
	print x
elif -900 <= diff2 <= 900:
	print ans(diff2)
elif -900 <= diff3 <= 900:
	print ans(diff3)
else:
	print 0
	