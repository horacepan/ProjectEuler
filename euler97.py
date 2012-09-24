
def get10( n ):
	s = str(n)
	if len(s) < 10:
		return n
	else:
		return int(s[len(s) - 10: len(s)])

def run(n, times):
	for i in range(0, times):
		print i	
		if len(str(n)) < 10:
			n = 2*n
		else:
			n = get10(2*n)
	return n
print run(28433, 7830457)