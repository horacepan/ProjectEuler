
def isPalindrome( n ):
	nstr = str(n)
	return nstr == nstr[::-1]

def isLych( n, k ):
	if k == 0:
		return isPalindrome( n )
	else:
		x`