import sys

n, k = [int(x) for x in sys.stdin.readline().split()]

print n*(n-1)/2 - k
