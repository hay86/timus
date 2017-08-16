# http://oeis.org/A000670
# http://en.wikipedia.org/wiki/Ordered_Bell_number
import sys

ans = [1, 1, 3, 13, 75, 541, 4683, 47293, 545835, 7087261, 102247563]

for line in sys.stdin:
	i = int(line)
	if i == -1:
		break
	print ans[i]
