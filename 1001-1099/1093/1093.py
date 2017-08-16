'''
plane formula: nx(x-px) + ny(y-py) + nz(z-pz) = 0
'''
import sys

px, py, pz, nx, ny, nz, r = [float(x) for x in sys.stdin.readline().split()]
sx, sy, sz, vx, vy, vz = [float(x) for x in sys.stdin.readline().split()]

ap, bp, cp, dp = nx, ny, nz, -nx*px-ny*py-nz*pz
ax, bx = vx, sx
ay, by = vy, sy
az, bz, cz = -5, vz, sz
a, b, c = az*cp, ax*ap+ay*bp+bz*cp, bx*ap+by*bp+cz*cp+dp

def hit(t):
	x, y, z = ax*t+bx, ay*t+by, az*t*t+bz*t+cz
	dist = (px-x)**2 + (py-y)**2 + (pz-z)**2
	return dist < r*r

if a == 0:
	if c*b < 0 and hit(-c/b):
		print 'HIT'
	else:
		print 'MISSED'
else:
	delta = b*b-4*a*c
	if delta < 0:
		print 'MISSED'
	else:
		t1, t2 = (-b+delta**0.5)/(2*a), (-b-delta**0.5)/(2*a)
		if t1 > 0 and hit(t1):
			print 'HIT'
		elif t2 > 0 and hit(t2):
			print 'HIT'
		else:
			print 'MISSED'
