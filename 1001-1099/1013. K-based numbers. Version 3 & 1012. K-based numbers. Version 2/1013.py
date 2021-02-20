import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
m = int(sys.stdin.readline())

a1, a2 = (k-1)%m, (k*(k-1))%m

# A = [0,k-1] = [a,b]
#     [1,k-1] = [c,d]
# [an-1,an] = [a1,a2]*A^^(n-2)

def pow(n, m, k):
	if n == 0:
		return 1,0,0,1
	a,b,c,d = pow(n/2, m, k)
	if n % 2 == 0:
		return (a*a+b*c)%m, (b*(a+d))%m, (c*(a+d))%m, (c*b+d*d)%m
	else:
		return (b*(a+d))%m, (a*a*(k-1)+b*(a+c+d)*(k-1))%m, (c*b+d*d)%m, (c*(a+b+d)*(k-1)+d*d*(k-1))%m

a,b,c,d = pow(n-2, m, k)
print (a1*b+a2*d)%m