
def triangle( n ):
	return (n*(n+1))/2
	
def pent( n ):
	return (n*(3*n - 1))/2
	
def hex( n ):
	return (n*(2*n-1))
	
tri = set(triangle(n) for n in range(100000))
pent = set(pent(n) for n in range(100000))
hex = set(hex(n) for n in range(100000))

hp = pent.intersection(hex)
thp = hp.intersection(tri)


for i in thp:
	print i


