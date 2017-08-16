import sys, math
from decimal import *
getcontext().prec=1000

num = int(sys.stdin.readline())*2
print int(Decimal(num).sqrt())
