def run():
	def isPandigital( n ):
		digits = set(str(i) for i in range(1,10))
		isPan = True
		for letter in n:
			if letter not in digits:
				isPan = False
				break
			else:
				digits.remove( letter )
		return isPan
	
	pandigits = set()
	#1 digit * 4 digit -> 4 digit 
	for i in range(2, 10):
		for j in range(1000, 10000):
			numstring = '%d%d%d' % (i, j, i*j)
			if isPandigital(numstring):
				print numstring
				pandigits.add(i*j)
	
	#2 digit * 3 digit -> 5 
	for i in range(10, 100):
		for j in range(100, 1000):
			numstring = '%d%d%d' % (i, j, i*j)
			if isPandigital(numstring):
				print numstring
				pandigits.add(i*j)
	
	print sum(pandigits)
			
if __name__ == '__main__':
	run()
