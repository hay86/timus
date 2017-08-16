import sys, math

v, a, k = [float(x) for x in sys.stdin.readline().split()]
vx = math.cos(math.radians(a)) * v
vy = math.sin(math.radians(a)) * v
t = 2*vy/10
s0 = t*vx
s = s0/(1-1/k)
print '%.2f' % s
