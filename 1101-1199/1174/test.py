n = 4
permut = range(n+1)
position = range(n+1)
dir = [-1]*(n+1)

def switch(p1, p2):
	xch = permut[p1]
	permut[p1] = permut[p2]
	permut[p2] = xch
	position[permut[p1]] = p1
	position[permut[p2]] = p2
	
def generatepermutation(nn):
	if nn == n+1:
		print permut
	else:
		generatepermutation(nn+1)
		for i in range(1, nn):
			switch(position[nn], position[nn]+dir[nn])
			generatepermutation(nn+1)
		dir[nn] = -dir[nn]
		
generatepermutation(1)