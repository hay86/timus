import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
num = [1]*(n+1)

for i in range(1,n):
	for j in range(i):
		if arr[i] > arr[j]:
			num[arr[i]] += 1
			
for i in range(2,n+1):
	num[i] = (num[i-1]-1)*i + (i-num[i]+1 if num[i-1]%2==1 else num[i])
	
print num[n]