import sys
from math import radians, sqrt, sin, cos, atan2

for i in range(3):
	sys.stdin.readline()
a = sys.stdin.readline()
b = sys.stdin.readline()
sys.stdin.readline()
c = sys.stdin.readline()
d = sys.stdin.readline()

def parse(str):
	str = str.strip()
	a = str.find('^')
	b = str.find("'")
	c = str.find('"')
	d = int(str[0:a])
	e = int(str[a+1:b])
	f = int(str[b+1:c])
	g = d + e/60.0 + f/3600.0
	if str[-2] == 'N' or str[-2] == 'E':
		return g
	else:
		return -g

def geocalc(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon1 - lon2

    EARTH_R = 6875/2.0

    y = sqrt(
        (cos(lat2) * sin(dlon)) ** 2
        + (cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)) ** 2
        )
    x = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon)
    c = atan2(y, x)
    return EARTH_R * c

a = parse(a)
b = parse(b.replace('and ', '').replace('.', ''))
c = parse(c)
d = parse(d.replace('and ', '').replace('.', ''))

dist = float('%.2f' % round(geocalc(a, b, c, d), 2))
print 'The distance to the iceberg: %.2f miles.' % dist
if dist < 100:
	print 'DANGER!'
