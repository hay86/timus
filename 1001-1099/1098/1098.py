import sys

text = []
for ch in sys.stdin.read():
	if ch != '\n' and ch != '\r':
		text.append(ch)

ans = [0]
for i in range(1, len(text)+1):
	ans.append((ans[i-1]+1999)%i)

ch = text[ans[len(text)]]
if ch == '?':
	print 'Yes'
elif ch == ' ':
	print 'No'
else:
	print 'No comments'
